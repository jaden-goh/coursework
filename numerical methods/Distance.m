function [d, p1, p2, th1, th2] = Distance(r1, ex1, ey1, r2, ex2, ey2, n)
% Computes the shortest distance between two identical superellipses
% using Newton’s method.
%
% Superellipse parameters:
%   {r1, a1=b1=1, n, ex1, ey1}, {r2, a2=b2=1, n, ex2, ey2}
%   2 < n ≤ 3.4
%
% Returns:
%   d   = shortest distance (0 if overlapping)
%   p1  = closest point on first
%   p2  = closest point on second
%   th1 = angle param on first
%   th2 = angle param on second

    % --- Parametric functions ---
    param = @(theta, n) [sign(cos(theta)) .* abs(cos(theta)).^(2/n);
                         sign(sin(theta)) .* abs(sin(theta)).^(2/n)];
    dparam = @(theta, n) [-(2/n)*sign(cos(theta)).*abs(cos(theta)).^(2/n-1).*sin(theta);
                           (2/n)*sign(sin(theta)).*abs(sin(theta)).^(2/n-1).*cos(theta)];

    % --- Normalize rotation frames ---
    ex1 = ex1 / norm(ex1); ey1 = ey1 / norm(ey1);
    ex2 = ex2 / norm(ex2); ey2 = ey2 / norm(ey2);
    R1 = [ex1(:), ey1(:)];
    R2 = [ex2(:), ey2(:)];

    % --- Coarse initialization by grid search ---
    theta = linspace(0, 2*pi, 40);
    min_d = inf; th1 = 0; th2 = 0;
    for t1 = theta
        p1t = r1(:) + R1*param(t1,n);
        for t2 = theta
            p2t = r2(:) + R2*param(t2,n);
            dtmp = norm(p1t - p2t);
            if dtmp < min_d
                min_d = dtmp; th1 = t1; th2 = t2;
            end
        end
    end

    % --- Newton refinement ---
    for k = 1:40
        p1 = r1(:) + R1*param(th1,n);
        p2 = r2(:) + R2*param(th2,n);
        diff = p1 - p2;

        g1 = R1*dparam(th1,n);
        g2 = R2*dparam(th2,n);

        F = [diff.'*g1; diff.'*(-g2)];
        J = [g1.'*g1, -g1.'*g2;
             g2.'*g1, -g2.'*g2];
        J = J + 1e-12*eye(2); % regularization

        delta = -J\F;
        alpha = 0.5; % damping factor
        th1 = th1 + alpha*delta(1);
        th2 = th2 + alpha*delta(2);

        if norm(F) < 1e-10
            break
        end
    end

    % --- Final results ---
    p1 = r1(:) + R1*param(th1,n);
    p2 = r2(:) + R2*param(th2,n);
    d = norm(p1 - p2);

    % --- Overlap detection (manual, no toolbox) ---
    if isOverlappingSimple(r1, R1, r2, R2, n)
        d = 0;
    end
end


function overlap = isOverlappingSimple(r1, R1, r2, R2, n)
% Manual overlap detection (no pdist2)
% Checks if any vertex of one superellipse is inside the other

    theta = linspace(0, 2*pi, 100);
    % Points on first superellipse (in world coords)
    SE1 = r1(:) + R1*[sign(cos(theta)).*abs(cos(theta)).^(2/n);
                      sign(sin(theta)).*abs(sin(theta)).^(2/n)];
    % Points on second
    SE2 = r2(:) + R2*[sign(cos(theta)).*abs(cos(theta)).^(2/n);
                      sign(sin(theta)).*abs(sin(theta)).^(2/n)];

    % Transform SE1 points into local frame of SE2
    invR2 = R2'; % since R2 is orthonormal
    localSE1 = invR2*(SE1 - r2(:));

    % Superellipse implicit function test:
    % F(x,y) = |x|^(n/2) + |y|^(n/2) <= 1  -> inside
    Fx = abs(localSE1(1,:)).^(n/2) + abs(localSE1(2,:)).^(n/2);
    inside12 = any(Fx <= 1 + 1e-3);

    % Symmetric check (points of SE2 in SE1 frame)
    invR1 = R1';
    localSE2 = invR1*(SE2 - r1(:));
    Fy = abs(localSE2(1,:)).^(n/2) + abs(localSE2(2,:)).^(n/2);
    inside21 = any(Fy <= 1 + 1e-3);

    overlap = inside12 || inside21;
end

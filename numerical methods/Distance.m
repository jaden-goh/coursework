function [d,p1,p2,th1,th2] = Distance(r1,a1,b1,n,ex1,ey1,r2,a2,b2,ex2,ey2)
    param = @(theta,a,b,n) [a*sign(cos(theta)).*abs(cos(theta)).^(2/n);
                            b*sign(sin(theta)).*abs(sin(theta)).^(2/n)];
    dparam = @(theta,a,b,n) [-(2*a/n)*sign(cos(theta)).*abs(cos(theta)).^(2/n-1).*sin(theta);
                              (2*b/n)*sign(sin(theta)).*abs(sin(theta)).^(2/n-1).*cos(theta)];
    
    ex1 = ex1/norm(ex1); ey1 = ey1/norm(ey1);
    ex2 = ex2/norm(ex2); ey2 = ey2/norm(ey2);
    R1 = [ex1(:), ey1(:)];
    R2 = [ex2(:), ey2(:)];
function [d, p1, p2, th1, th2] = SuperellipseDistance(r1, ex1, ey1, r2, ex2, ey2, n)
% Computes the shortest distance between two identical superellipses
% using Newton’s method.
%
% Superellipse parameters:
% {r1, a1=b1=1, n, ex1, ey1}, {r2, a2=b2=1, n, ex2, ey2}
% with 2 < n ≤ 3.4
%
% Returns:
%   d   = shortest distance (0 if overlapping)
%   p1  = point on first superellipse
%   p2  = point on second superellipse
%   th1 = parameter on first
%   th2 = parameter on second

    % Parameterization and derivatives
    param = @(theta, n) [sign(cos(theta)) .* abs(cos(theta)).^(2/n);
                         sign(sin(theta)) .* abs(sin(theta)).^(2/n)];
    dparam = @(theta, n) [-(2/n)*sign(cos(theta)).*abs(cos(theta)).^(2/n-1).*sin(theta);
                           (2/n)*sign(sin(theta)).*abs(sin(theta)).^(2/n-1).*cos(theta)];

    % Normalize orientation vectors
    ex1 = ex1 / norm(ex1);
    ey1 = ey1 / norm(ey1);
    ex2 = ex2 / norm(ex2);
    ey2 = ey2 / norm(ey2);
    R1 = [ex1(:), ey1(:)];
    R2 = [ex2(:), ey2(:)];

    % --- Initial coarse grid search ---
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

    % --- Newton's iteration ---
    for k = 1:40
        p1 = r1(:) + R1*param(th1,n);
        p2 = r2(:) + R2*param(th2,n);
        diff = p1 - p2;

        g1 = R1*dparam(th1,n);
        g2 = R2*dparam(th2,n);

        F = [diff.'*g1; diff.'*(-g2)];
        J = [g1.'*g1, -g1.'*g2; g2.'*g1, -g2.'*g2];
        J = J + 1e-12*eye(2);

        delta = -J\F;
        alpha = 0.5; % damping
        th1 = th1 + alpha*delta(1);
        th2 = th2 + alpha*delta(2);

        if norm(F) < 1e-10
            break;
        end
    end

    % --- Final distance ---
    p1 = r1(:) + R1*param(th1,n);
    p2 = r2(:) + R2*param(th2,n);
    d = norm(p1 - p2);

    % If overlapping, set distance = 0
    if isOverlapping(r1, R1, r2, R2, n)
        d = 0;
    end
end


function overlap = isOverlapping(r1, R1, r2, R2, n)
% Rough overlap detection via sampling
    theta = linspace(0, 2*pi, 200);
    SE1 = r1(:) + R1*[sign(cos(theta)).*abs(cos(theta)).^(2/n);
                      sign(sin(theta)).*abs(sin(theta)).^(2/n)];
    SE2 = r2(:) + R2*[sign(cos(theta)).*abs(cos(theta)).^(2/n);
                      sign(sin(theta)).*abs(sin(theta)).^(2/n)];

    % Distance between all points (approximate)
    D = pdist2(SE1.', SE2.');
    overlap = any(D(:) < 1e-3);  % tolerance threshold
end

    % Initial grid search
    theta = linspace(0,2*pi,50);
    min_d = inf;
    for t1 = theta
        for t2 = theta
            p1t = r1(:) + R1*param(t1,a1,b1,n);
            p2t = r2(:) + R2*param(t2,a2,b2,n);
            dtmp = norm(p1t - p2t);
            if dtmp < min_d
                min_d = dtmp; th1 = t1; th2 = t2;
            end
        end
    end

    for k = 1:40
        p1 = r1(:) + R1*param(th1,a1,b1,n);
        p2 = r2(:) + R2*param(th2,a2,b2,n);
        diff = p1 - p2;
        g1 = R1*dparam(th1,a1,b1,n);
        g2 = R2*dparam(th2,a2,b2,n);
        F = [diff.'*g1; diff.'*(-g2)];
        J = [g1.'*g1, -g1.'*g2; g2.'*g1, -g2.'*g2];
        J = J + 1e-12*eye(2); % regularize
        delta = -J\F;
        th1 = th1 + 0.5*delta(1);
        th2 = th2 + 0.5*delta(2);
        if norm(F) < 1e-10, break; end
    end

    p1 = r1(:) + R1*param(th1,a1,b1,n);
    p2 = r2(:) + R2*param(th2,a2,b2,n);
    d = norm(p1-p2);

    % Plot
    hold on; axis equal
    theta = linspace(0,2*pi,400);
    SE1 = r1(:) + R1*[a1*sign(cos(theta)).*abs(cos(theta)).^(2/n);
                      b1*sign(sin(theta)).*abs(sin(theta)).^(2/n)];
    SE2 = r2(:) + R2*[a2*sign(cos(theta)).*abs(cos(theta)).^(2/n);
                      b2*sign(sin(theta)).*abs(sin(theta)).^(2/n)];
    plot(SE1(1,:), SE1(2,:), 'b','LineWidth',1.5)
    plot(SE2(1,:), SE2(2,:), 'k','LineWidth',1.5)
    plot([p1(1),p2(1)], [p1(2),p2(2)], 'ro-','LineWidth',2)
end

function [d_best, p1_best, p2_best] = Distance(r1,a1,b1,n,ex1,ey1,r2,a2,b2,n2,ex2,ey2)

tol = 1e-10;
maxIter = 200;
numStarts = 20; % no. random initial guesses

d_best = inf;
p1_best = [NaN; NaN];
p2_best = [NaN; NaN];

for trial = 1:numStarts
    theta1 = 2*pi*rand();
    theta2 = 2*pi*rand();
    
    for k = 1:maxIter
        [p1, dp1, d2p1] = paramPoint(r1, ex1, ey1, a1, b1, n, theta1);
        [p2, dp2, d2p2] = paramPoint(r2, ex2, ey2, a2, b2, n2, theta2);
        diff = p1 - p2;
        
        % gradient and Hessian of D = ||p1 - p2||^2
        g1 = 2 * (diff' * dp1);
        g2 = -2 * (diff' * dp2);
        H11 = 2 * (dp1' * dp1 + diff' * d2p1);
        H22 = 2 * (dp2' * dp2 + diff' * d2p2);
        H12 = -2 * (dp1' * dp2);
        
        g = [g1; g2];
        H = [H11 H12; H12 H22];
        
        % convergence check
        if norm(g) < tol
            break;
        end
        
        % Newton step
        if rcond(H) < 1e-10 || any(isnan(H(:)))
            break; 
        end
        dtheta = -H \ g;
        
        % damping
        alpha = 1.0;
        success = false;
        while alpha > 1e-3
            t1n = theta1 + alpha*dtheta(1);
            t2n = theta2 + alpha*dtheta(2);
            [q1,~,~] = paramPoint(r1, ex1, ey1, a1, b1, n, t1n);
            [q2,~,~] = paramPoint(r2, ex2, ey2, a2, b2, n2, t2n);
            if norm(q1 - q2) < norm(p1 - p2)
                theta1 = t1n; theta2 = t2n;
                success = true;
                break;
            else
                alpha = alpha/2;
            end
        end
        if ~success, break; end
    end
    
    % evaluate against best
    [p1,~,~] = paramPoint(r1, ex1, ey1, a1, b1, n, theta1);
    [p2,~,~] = paramPoint(r2, ex2, ey2, a2, b2, n2, theta2);
    d = norm(p1 - p2);
    
    if d < d_best
        d_best = d;
        p1_best = p1;
        p2_best = p2;
    end
end

% overlap check
if d_best < 1e-6
    d_best = 0;
end
end

% ---- param point and derivatives ----
function [p, dp, d2p] = paramPoint(r, ex, ey, a, b, n, t)
c = cos(t); s = sin(t);
m = 2/n;
signc = sign(c); signs = sign(s);
abs_c = abs(c); abs_s = abs(s);

% point
u = a * signc * abs_c^m;
v = b * signs * abs_s^m;
p = r + u*ex + v*ey;

% first derivative
du = (2*a/n) * abs_c^(m-1) * (-s);
dv = (2*b/n) * abs_s^(m-1) * (c);
dp = du*ex + dv*ey;

% second derivative
d2u = (2*a/n)*((m-1)*abs_c^(m-2)*(c*s) - abs_c^(m-1)*cos(t));
d2v = (2*b/n)*((m-1)*abs_s^(m-2)*(s*c) - abs_s^(m-1)*sin(t));
d2p = d2u*ex + d2v*ey;
end
    
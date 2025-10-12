function d = Distance(r1,a1,b1,n,ex1,ey1,r2,a2,b2,~,ex2,ey2)
    % Function
    param = @(theta,a,b,n) [a*sign(cos(theta))*abs(cos(theta))^(2/n);
                            b*sign(sin(theta))*abs(sin(theta))^(2/n)];

    % Derivative 
    dparam = @(theta,a,b,n) [-(2*a/n)*sign(cos(theta))*abs(cos(theta))^(2/n-1)*sin(theta);
                              (2*b/n)*sign(sin(theta))*abs(sin(theta))^(2/n-1)*cos(theta)];

    R1 = [ex1(:), ey1(:)];
    R2 = [ex2(:), ey2(:)];

    th1 = 0.5; th2 = 1.0;    % initial guesses

    for k = 1:30
        p1 = r1(:) + R1*param(th1,a1,b1,n);
        p2 = r2(:) + R2*param(th2,a2,b2,n);
        diff = p1 - p2;

        g1 = R1*dparam(th1,a1,b1,n);
        g2 = R2*dparam(th2,a2,b2,n);

        % Build system F = 0
        F = [diff'*g1; diff'*(-g2)];
        J = [g1'*g1, -g1'*g2;
             g2'*g1, -g2'*g2];

        delta = -J\F;
        th1 = th1 + delta(1);
        th2 = th2 + delta(2);
    end

    % Final closest points
    p1 = r1(:) + R1*param(th1,a1,b1,n);
    p2 = r2(:) + R2*param(th2,a2,b2,n);
    d = norm(p1-p2);

    % Draw line between closest points
    hold on;
    plot([p1(1),p2(1)],[p1(2),p2(2)],'ro-','LineWidth',2);
end

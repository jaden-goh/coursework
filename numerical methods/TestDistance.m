clc; clear; close all;

% Fixed parameters from Table 1
r1  = [0; 0];
ex1 = [1; 0];
ey1 = [0; 1];
a1 = 1; b1 = 1; a2 = 1; b2 = 1;

% Table 1 data:  r2, ex2, ey2, n
cases = {
    [1.7532;  2.7570], [-0.9268;  0.3754], [-0.3754; -0.9268], 2.5;
    [0.9344; -2.7857], [-0.7356;  0.6774], [-0.6774; -0.7356], 3.0;
    [2.0948;  2.6040], [ 0.0973; -0.9953], [ 0.9953;  0.0973], 3.4;
    [-1.3385; -2.7230],[ 0.2802; -0.9599], [ 0.9599;  0.2802], 3.5;
};

for i = 1:size(cases,1)
    r2  = cases{i,1};
    ex2 = cases{i,2};
    ey2 = cases{i,3};
    n   = cases{i,4};

    fprintf('\nCase %02d — n = %.1f\n', i, n);
    [d, p1, p2, th1, th2] = Distance(r1, ex1, ey1, r2, ex2, ey2, n);
    fprintf('Shortest distance = %.6f\n', d);

    % Plot geometry
    theta = linspace(0, 2*pi, 400);
    R1 = [ex1 ey1]; R2 = [ex2 ey2];
    SE1 = r1 + R1*[sign(cos(theta)).*abs(cos(theta)).^(2/n);
                   sign(sin(theta)).*abs(sin(theta)).^(2/n)];
    SE2 = r2 + R2*[sign(cos(theta)).*abs(cos(theta)).^(2/n);
                   sign(sin(theta)).*abs(sin(theta)).^(2/n)];
    figure('Color','w');
    hold on; axis equal; grid on;
    plot(SE1(1,:), SE1(2,:), 'b', 'LineWidth', 1.5);
    plot(SE2(1,:), SE2(2,:), 'k', 'LineWidth', 1.5);
    plot([p1(1), p2(1)], [p1(2), p2(2)], 'ro-', 'LineWidth', 2);
    plot(p1(1), p1(2), 'bs', 'MarkerFaceColor','b');
    plot(p2(1), p2(2), 'ks', 'MarkerFaceColor','k');
    title(sprintf('Case %d  n = %.1f  d = %.4f', i, n, d));
    xlabel('x'); ylabel('y');
end

%% test_distance_superellipses.m
clc; clear; close all;

% Helper to build rotation frame from angle
rot_frame = @(ang) deal([cos(ang); sin(ang)], [-sin(ang); cos(ang)]);

% List of handcrafted test cases
% Each entry: [desc, r1, a1, b1, n1, ang1, r2, a2, b2, n2, ang2]
% Note: Distance() uses a single n for both shapes; set n = mean(n1,n2) if you want variety.
tests = {
% 1) Simple, axis-aligned ellipses (n=2), clearly separated
'Axis-aligned ellipses, separated', [0;0], 2, 1, 2, 0,  [4;0.5], 1, 0.7, 2, pi/12;

% 2) Rotated vs axis-aligned, close to tangent
'Near-tangent, rotated vs axis-aligned', [0;0], 2.0, 0.8, 2, 0,  [2.9;0.1], 1.1, 0.9, 2, pi/5;

% 3) Super-rectangle (n~1.3) vs supercircle (n=4)
'Super-rectangle vs supercircle', [0;0], 1.5, 1.0, 1.3, pi/8,  [3.0;0.0], 1.0, 1.0, 4.0, pi/4;

% 4) Skinny vs fat, both rotated
'Skinny vs fat, both rotated', [0;0], 2.5, 0.5, 2, pi/7,  [3.2;1.5], 0.8, 1.8, 2, -pi/6;

% 5) Overlapping shapes (expect ~0 distance)
'Overlapping (expect ~0)', [0;0], 2.0, 1.2, 2, pi/12,  [0.5;0.3], 1.6, 1.1, 2, -pi/8;

% 6) Nearly parallel edges (hard case), small gap
'Nearly parallel edges, tiny gap', [0;0], 2.0, 0.6, 1.5, 0,  [2.7;0.02], 2.0, 0.6, 1.5, 0.02;

% 7) Far apart, rotated
'Far apart, rotated', [-5;3], 1.2, 0.9, 3.5, pi/3,  [7;-4], 1.1, 1.0, 3.5, -pi/9;

% 8) Small shapes, random rotations, small separation
'Small shapes, small separation', [0;0], 0.7, 0.5, 2.5, pi/10,  [1.4;0.2], 0.6, 0.6, 2.5, pi/3;

% 9) Very round (n=10) vs squarish (n=1.2)
'Round (n=10) vs squarish (n=1.2)', [0;0], 1.3, 1.3, 10, pi/6,  [2.6;0.6], 1.2, 0.9, 1.2, -pi/12;

% 10) Long skinny both, slight skew and offset
'Long skinny both, skewed', [0;0], 3.2, 0.4, 2, pi/20,  [3.6;0.25], 3.1, 0.45, 2, -pi/18;
};

% --- Run handcrafted tests with plots ---
for i = 1:size(tests,1)
    desc = tests{i,1};
    r1 = tests{i,2}; a1 = tests{i,3}; b1 = tests{i,4}; n1 = tests{i,5}; ang1 = tests{i,6};
    r2 = tests{i,7}; a2 = tests{i,8}; b2 = tests{i,9}; n2 = tests{i,10}; ang2 = tests{i,11};

    % Use a single n in Distance(). If you want asymmetric n, you can
    % try n = (n1 + n2)/2 as a compromise for testing visuals.
    n = (n1 + n2)/2;

    [ex1, ey1] = rot_frame(ang1);
    [ex2, ey2] = rot_frame(ang2);

    figure('Color','w'); hold on; axis equal; grid on;
    title(sprintf('[%02d] %s', i, desc), 'Interpreter', 'none');

    % Call your Distance() which should also draw the connecting segment
    [d, p1, p2, th1, th2] = Distance(r1,a1,b1,n,ex1,ey1,r2,a2,b2,ex2,ey2);

    % Add markers for closest points
    plot(p1(1), p1(2), 'bs', 'MarkerFaceColor','b', 'DisplayName','p1');
    plot(p2(1), p2(2), 'ks', 'MarkerFaceColor','k', 'DisplayName','p2');

    % Label & annotate
    xlabel('x'); ylabel('y');
    legend({'Closest segment','p1','p2'}, 'Location','best');
    text(mean([p1(1),p2(1)]), mean([p1(2),p2(2)]), ...
         sprintf(' d = %.6f', d), 'BackgroundColor',[1 1 1 0.7], 'Margin',4);

    % Adjust view a bit
    axis tight;
    pad = 0.5;
    xl = xlim; yl = ylim;
    xlim(xl + [-pad pad]); ylim(yl + [-pad pad]);

    drawnow;
end

%% --- Random stress tests (no plotting) ---
rng(1);
fprintf('\nRandom stress tests (no plots):\n');
for k = 1:15
    % Random centers within a box
    r1 = 4*(rand(2,1)-0.5);
    r2 = 4*(rand(2,1)-0.5) + [2; 0.5].*randn(2,1);

    % Random axes lengths
    a1 = 0.5 + 2.5*rand; b1 = 0.4 + 1.6*rand;
    a2 = 0.5 + 2.5*rand; b2 = 0.4 + 1.6*rand;

    % Random exponents (squarish to round)
    n = 1.1 + 4.0*rand;

    % Random rotations
    ang1 = 2*pi*rand; ang2 = 2*pi*rand;
    [ex1, ey1] = rot_frame(ang1);
    [ex2, ey2] = rot_frame(ang2);

    % Compute
    try
        [d, ~, ~, ~, ~] = Distance(r1,a1,b1,n,ex1,ey1,r2,a2,b2,ex2,ey2);
        fprintf('  Test %02d: d = %.6f | n=%.2f | a1=%.2f b1=%.2f | a2=%.2f b2=%.2f\n', ...
            k, d, n, a1, b1, a2, b2);
    catch ME
        fprintf('  Test %02d: FAILED (%s)\n', k, ME.message);
    end
end

fprintf('\nDone. Inspect the figures for geometric sanity and the console for random test distances.\n');

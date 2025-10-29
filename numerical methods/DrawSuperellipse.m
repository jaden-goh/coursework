function DrawSuperellipse(r0,a,b,n,ex,ey)
    N = 400;                     % number of points
    h = 2*pi/N;                  % step size
    theta = 0;
    pts = zeros(N,2);

    for i = 1:N
        % Midpoint RK2 method
        k1x = a*sign(cos(theta))*abs(cos(theta))^(2/n);
        k1y = b*sign(sin(theta))*abs(sin(theta))^(2/n);

        mid_theta = theta + h/2;
        k2x = a*sign(cos(mid_theta))*abs(cos(mid_theta))^(2/n);
        k2y = b*sign(sin(mid_theta))*abs(sin(mid_theta))^(2/n);

        % Use midpoint estimate
        pts(i,:) = [k2x, k2y];
        theta = theta + h;
    end

    % Rotation
    R = [ex(:), ey(:)];
    pts_rot = (R*pts')';

    % Translate to r0
    pts_final = pts_rot + repmat(r0(:)', size(pts_rot,1), 1);

    plot(pts_final(:,1),pts_final(:,2),'k-','LineWidth',2);
    axis equal;
end

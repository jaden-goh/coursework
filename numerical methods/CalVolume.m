function S = CalVolume(a,b,n)
    N = 10000;                    % number of subdivisions
    dx = a/N;
    sum_val = 0;

    for i = 1:N
        x_left = (i-1)*dx;
        x_right = i*dx;

        % function y(x) = b * (1 - (x/a)^n)^(1/n)
        y_left = b*(1 - (x_left/a)^n)^(1/n);
        y_right = b*(1 - (x_right/a)^n)^(1/n);

        sum_val = sum_val + 0.5*(y_left + y_right)*dx;
    end

    % full area (4 quadrants)
    S = 4*sum_val;
end

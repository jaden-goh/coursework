% This function implements an adaptive Runge-Kutta 2nd order method to solve
% an ordinary differential equation (ODE) with a variable step size.
%
% The adaptive nature of the method allows the step size 'h' to be adjusted
% to maintain a desired level of accuracy, defined by 'eps'.
%
% Inputs:
% xmin: The starting x-value.
% xmax: The ending x-value.
% eps: The tolerance for the error.
% y0: The initial y-value at xmin.
function adaptiveRK2(xmin, xmax, eps, y0)
    % Initialize variables.
    h0 = 1;          % Initial step size
    xi = xmin;       % Current x-value
    yi = y0;         % Current y-value
    NMAX = 10000;    % Maximum number of steps to prevent infinite loops
    
    % Pre-allocate arrays to store the solution points.
    xn = zeros(NMAX, 1);
    yn = zeros(NMAX, 1);
    
    % Initialize step counter and store the first point.
    N = 1;
    xn(N) = xi;
    yn(N) = yi;
    
    % Main loop: Continue until the end of the range is reached.
    while (xi < xmax)
        % Set the initial guess for the step size.
        h = 2 * h0;
        
        % Inner loop: Adjust the step size 'h' until the error is within the tolerance.
        err = 1.0; % Initialize error to a value larger than eps
        while (err > eps)
            % Reduce the step size by half.
            h = h * 0.5;
            
            % Method 1: Perform one step of RK2 with step size 'h'.
            % This is for the less accurate solution.
            xh1 = xi + 0.5 * h;
            yh1 = yi + odefun2(xi, yi) * 0.5 * h;
            yi1 = yi + odefun2(xh1, yh1) * h;
            
            % Method 2: Perform two steps of RK2 with step size 'h/2'.
            % This is for the more accurate solution.
            h2 = h * 0.5;
            
            % First sub-step.
            xh2 = xi + 0.5 * h2;
            yh2 = yi + odefun2(xi, yi) * 0.5 * h2;
            ym = yi + odefun2(xh2, yh2) * h2; xm = xi + h2;
            
            % Second sub-step.
            xh2 = ym + 0.5 * h2;
            yh2 = ym + odefun2(xm, ym) * 0.5 * h2;
            yi2 = ym + odefun2(xh2, yh2) * h2;
            
            % Calculate the error as the absolute difference between the two solutions.
            err = abs(yi1 - yi2);
        end
        
        % After finding an acceptable step size, store the new point.
        if (N + 1 <= NMAX)
            N = N + 1;
            xn(N) = xi + h;
            yn(N) = yi1;
            xi = xi + h;
            yi = yi1;
        else
            % Handle the case where the maximum number of steps is exceeded.
            disp('NMAX is too small!');
            exit;
        end
    end
    
    % Extract the valid parts of the arrays and plot the result.
    xx = xn(1:N);
    yy = yn(1:N);
    plot(xx, yy, 'bo-');
end

% A placeholder function for the derivative dy/dx = f(x,y).
% You need to replace this with your actual ODE function.
    function f = odefun2(x, y)
        f = -2 * x^6 + 12 * x^2 - 20 * x + 8.5;
    end


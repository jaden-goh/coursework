% This function implements the midpoint method (also known as the modified Euler method)
% to solve an ordinary differential equation (ODE) numerically.
% It then plots the numerical solution against a known analytical solution.
%
% Inputs:
% xmin: The starting value of x.
% xmax: The ending value of x.
% h: The step size.
% y0: The initial condition for y at xmin.
function middlepoint(xmin, xmax, h, y0)
    % Calculate the number of steps required to cover the range [xmin, xmax].
    nbin = round((xmax - xmin) / h);
    
    % Pre-allocate arrays to store the x and y values of the numerical solution.
    xn = zeros(nbin, 1);
    yn = zeros(nbin, 1);
    
    % Loop through each step to compute the solution.
    for i = 1:1:nbin
        % Calculate the x-value for the current step.
        xn(i) = xmin + (i - 1) * h;
        
        % Set the initial condition for the first point.
        if (i == 1)
            yn(i) = y0;
        else
            % Step 1: Predict the midpoint.
            % Calculate the x-value at the midpoint of the current interval.
            xihalf = xn(i - 1) + 0.5 * h;   
            
            % Use the Euler method to estimate the y-value at the midpoint.
            yihalf = yn(i - 1) + odefun(xn(i - 1), yn(i - 1)) * 0.5 * h;
            
            % Step 2: Correct the next y-value.
            % Use the derivative at the midpoint (xihalf, yihalf) to get a more
            % accurate estimate for the next y-value.
            yn(i) = yn(i - 1) + odefun(xihalf, yihalf) * h;
        end
    end
    
    % Plot the numerical solution points as blue circles.
    plot(xn, yn, "bo");
    
    % Define the analytical solution for comparison.
    x = xn;
    y = -0.5 * x.^4 + 4 * x.^3 - 10 * x.^2 + 8.5 * x + 1;
    
    % Keep the current plot so the analytical solution can be added.
    hold on;
    
    % Plot the analytical solution as a solid red line.
    plot(x, y, 'r-');
    
    % Define the ordinary differential equation (ODE) function.
    % This is dy/dx = f(x,y).
    function f = odefun(x, y)
        f = -2 * x^3 + 12 * x^2 - 20 * x + 8.5;
    end
end

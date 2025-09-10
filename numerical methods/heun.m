% Heun's method for solving ordinary differential equations.
% This function plots the numerical solution and a given analytical solution.
% 'xmin', 'xmax' define the range, 'h' is the step size, and 'y0' is the initial condition.
function heun(xmin, xmax, h, y0)
    % Calculate the number of steps based on the range and step size.
    nbin = round((xmax - xmin) / h);
    % Pre-allocate arrays for the numerical solution 'xn' and 'yn'.
    xn = zeros(nbin, 1);
    yn = zeros(nbin, 1);
    % Loop to compute the solution using Heun's method.
    for i = 1:nbin
        % Calculate the x-value for the current step.
        xn(i) = xmin + (i - 1) * h;
        % Set the initial condition for the first step.
        if (i == 1)
            yn(i) = y0;
        else
            % Heun's method predicts and then corrects the next y-value.
            % xi1 is the predicted y-value using Euler's method.
            xi1 = xn(i - 1) + h;
            % yi1 is the predicted y-value using Euler's method.
            yi1 = yn(i - 1) + h * odefun(xn(i - 1), yn(i - 1));
            
            % The corrected y-value is the average of the two slopes.
            yn(i) = yn(i - 1) + 0.5 * h * (odefun(xn(i - 1), yn(i - 1)) + odefun(xi1, yi1));
        end
    end

    % Plot the numerical solution in blue circles.
    plot(xn, yn, 'bo');
    % Hold the current plot so that the next plot command doesn't overwrite it.
    hold on;

    % Define and plot an analytical function for comparison.
    x = xn;
    y = -0.5 * x.^4 + 4 * x.^3 - 10 * x.^2 + 8.5 * x + 1;
    % Plot the analytical solution as a red line.
    plot(x, y, 'r-');

    % Add labels and a title to the plot.
    xlabel('x');
    ylabel('y');
    title('Heun''s Method and Analytical Solution');
    legend('Heun''s Method', 'Analytical Solution');
    grid on;
    % Release the hold state so subsequent plot commands start a new figure.
    hold off;
end
% A simple function representing the right-hand side of the ODE: dy/dx = f(x,y)
% This is a placeholder and should be replaced with the actual function for your ODE.
function f = odefun(x, y)
    % Example function: dy/dx = 2x - y
    f = 2 * x - y;
end

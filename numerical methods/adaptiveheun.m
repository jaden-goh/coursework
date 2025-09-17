% Heun's method for solving ordinary differential equations.
% This function plots the numerical solution and a given analytical solution.
% 'xmin', 'xmax' define the range, 'h' is the step size, and 'y0' is the initial condition.
function heun(xmin, xmax, eps, y0)
    % Calculate the number of steps based on the range and step size.
    h0 = 1; % Initial Step Size
    
    % Pre-allocate arrays for the numerical solution 'xn' and 'yn'.
    max = 10000;
    xn = zeros(max, 1);
    yn = zeros(max, 1);
    
    
    N = 1;
    xn(N) = xmin;
    yn(N) = y0;

    xi = xmin;
    yi = y0;

% Loop to compute the solution using Heun's method.
   while (xi < xmax)
        h = 2*h0;

        err = 1.0;
        while (err > eps)

            h = h*0.5;
            ytemp = yi + h * odefun(xi,yi);
            yi1 = yi + h * (odefun(xi,yi) + odefun(xi+h, ytemp)) * 0.5;

            h2 = h*0.5; % now half the other step size
            ytemp1 = yi + h2 * odefun(xi,yi);
            xmid = xi + h2;
            ymid = yi + h2 * 0.5 * (odefun(xi,yi) + odefun(xi+h2, ytemp1));
            ytemp2 = ymid + h2 *odefun(xmid, ymid);
            yi2 = yi + h2 * 0.5 * (odefun(xmid,ymid)+ odefun(xmid+h2, ytemp2));

            err = abs(yi1-yi2);
        end

        if (N+1 <= nmax)
            N = N + 1;
            xn(N) = xi + h;
            yn(N) = yi1;
            xi = xi + h;
            yi = yi1;
        else
            disp('NMAX too small');
            exit; 
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

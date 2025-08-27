function [ak_final, iterations] = GaussNewtonMethod()

    % --- 1. Data and Initial Parameters ---
    % Given data points (x, y) to be fitted
    xn = [0.038, 0.194, 0.425, 0.626, 1.253, 2.500, 3.740];
    yn = [0.050, 0.127, 0.094, 0.2122, 0.2729, 0.2665, 0.3317];
    
    % Initial guess for the parameters [a0, a1]
    a0 = [0.5; 0.1];
    
    % Initialize parameter vectors
    ak = a0;
    ak1 = a0;
    
    % --- 2. Control Parameters ---
    % Tolerance for the convergence criterion
    eps = 0.000001;
    
    % Counter for the number of iterations
    step = 0;
    
    % --- 3. The Gauss-Newton Iteration Loop ---
    % The loop continues as long as the norm of the change in parameters is
    % greater than the tolerance OR it is the first step (step == 0)
    while (norm(ak - ak1) > eps || step == 0)
        
        % Store the current parameter values for comparison in the next iteration
        ak = ak1;
        
        % Calculate the error vector 'e' at the current parameters 'ak'
        % e(i) = yi - f(xi, ak)
        e = calEvec(xn, yn, ak);
        
        % Calculate the Jacobian matrix 'J'
        % J(i,j) = df(xi, ak)/daj
        J = calJmatrix(xn, ak);
        
        % Calculate the update step 'Delta' using the Gauss-Newton formula
        % Delta = -inv(J' * J) * J' * e
        Delta = -inv(J' * J) * J' * e;
        
        % Update the parameters for the next iteration
        ak1 = ak + Delta;
        
        % Increment the step counter
        step = step + 1;
        
        % Display intermediate results for monitoring progress
        fprintf('Iteration: %d, Current parameters [a0; a1]: [%f; %f]\n', step, ak1(1), ak1(2));
    end
    
    % --- 4. Final Result ---
    % Assign the final converged parameters and iteration count to the output variables
    ak_final = ak1;
    iterations = step;
    
    % Display the final result
    fprintf('\nConvergence reached!\n');
    fprintf('Final parameters [a0; a1]: [%f; %f]\n', ak_final(1), ak_final(2));
    fprintf('Total iterations: %d\n', iterations);
end

% This function calculates the error vector 'e' for the Gauss-Newton algorithm.
% e is the difference between the observed data (yn) and the model's prediction.
%
% Inputs:
%   xn - The vector of x-values.
%   yn - The vector of observed y-values.
%   ak - The current parameter vector [a0; a1].
%
% Output:
%   e - The column vector of errors.
function e = calEvec(xn, yn, ak)
    % Get the number of data points.
    n = length(xn);
    
    % Initialize the error vector as a column vector of zeros.
    e = zeros(n, 1);
    
    % The assumed model function is f(x) = a0*x / (a1 + x).
    % The error is calculated as: e_i = y_i - f(x_i, ak)
    for i = 1 : n
        e(i) = yn(i) - ((xn(i) * ak(1)) / (ak(2) + xn(i)));
    end
end

% This function calculates the Jacobian matrix 'J' for the Gauss-Newton algorithm.
% J contains the partial derivatives of the model function with respect to the
% parameters a0 and a1.
%
% Inputs:
%   xn - The vector of x-values.
%   ak - The current parameter vector [a0; a1].
%
% Output:
%   J - The Jacobian matrix.
function J = calJmatrix(xn, ak)
    % Get the number of data points.
    n = length(xn);
    
    % Initialize the Jacobian matrix with dimensions n x 2.
    J = zeros(n, 2);
    
    % The assumed model function is f(x, a0, a1) = a0*x / (a1 + x).
    % The partial derivatives are:
    % df/da0 = x / (a1 + x)
    % df/da1 = -a0*x / (a1 + x)^2
    
    for i = 1 : n
        % First column of J: Partial derivative with respect to a0
        J(i, 1) = xn(i) / (ak(2) + xn(i));
        
        % Second column of J: Partial derivative with respect to a1
        J(i, 2) = (-ak(1) * xn(i)) / ((ak(2) + xn(i))^2);
    end
end

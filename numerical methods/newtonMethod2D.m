function newtonMethod2D(xi) % xi is a 1x2 matrix
    eps = 10e-6;
    maxiter = 10000;
    xi1 = xi;

    for i = 1:maxiter
        xi = xi1;
        xi1 = xi - (hessian(xi))\gradient(xi);
        if norm(xi1-xi) <eps; 
            steps = i;
            break
        end
    end
    [xi1, steps]
end


function gradient(x)
    %insert function first derivative
end 

function hessian(x)
    %insert function second derivative
end
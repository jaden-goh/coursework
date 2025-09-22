function curvefitting(xn, yn, a0) %xdata, ydata, starting coefficients
    a1 = a0;
    eps = 10e-6;
    maxiter = 1000;
    
    for i = 1:maxiter
        a0 = a1;
        e = calculateError(xn,yn,a0);
        j = calculateJacobian(xn,yn,a0);
        delta = -(J'*J)\J'*e;
        a1 = a0 + delta;

        if norm(a0-a1) < eps;
            steps = i;
            break
        end
    end

     [a0, steps]
end

function e = calculateError(xn,yn,a)
    n = length(xn);
    e = zeroes(n,1);
    for i = 1:n
            e(i) = (- (yn(i))) + a(1)*(xn(i))+a(2)*(xn(i)); % insert function here, take function of x minus y value, simple
    end
end

function J = calculateJacobian(xn,yn,a)
    n = length(xn);
    j = zeroes(n,2) % 2 coefficients, 2 columns 
    for i = 1:n
        j(i,1) = xn(i)*a(2);  % derivative w.r.t a(1)
        j(i,2) = xn(i)*a(1); % derivative w.r.t a(2)
    end
end
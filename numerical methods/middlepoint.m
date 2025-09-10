function middlepoint(xmin, xmax, h, y0)
    nbin = round((xmax-xmin)/h);
    xn = zeros(nbin,1);
    yn = zeros(nbin,1);
    for i = 1:1:nbin
        xn(i) = xmin + (i-1)*h
        if(i==1)
            yn(i) = y0;
        else
            xihalf = xn(i-1) + 0.5*h;
            yihalf = yn(i-1) + odefun (xn(i-1), yn(i-1)) * 0.5 * h;
            yn(i) = yn(i-1) + odefun (xihalf, yihalf) * h
        end
    end

    plot(xn,yn,"bo");
    x = xn;
    y = -0.5 * x.^4 + 4 * x.^3 - 10 * x.^2 + 8.5 * x + 1;
    hold on;
    plot(x,y,'r-')
    
    function f=odefun(x,y)
    f = -2 * x^3 + 12 * x ^2 - 20 * x +8.5;
function goldenSectionSearch(xl, xu)

    max_iter = 100;
    eps = 10e-6;
    ratio = (sqrt(5) - 1) / 2;
    
    for i = 1:max_iter
        
        x1 = xl + ratio*(xu-xl);
        x2 = xu - ratio*(xu-xl);

        fx1 = funct(x1); fx2 = funct(x2); % separate function 
        if fx1 > fx2
            xu = x1;
        else
            xl = x2;
        end

        if (xu-xl)>eps
            steps = i;
            break
        end
        
        
    end
    
    final = (xl+xu)/2;
    [final, funct(final), steps]
end

function funct(x)
    return % insert function here
end
% Parameters
a = 2; 
b = 1;
n_vals = 2:0.5:10;     % range of n
S_num = zeros(size(n_vals));
S_ana = zeros(size(n_vals));

for i = 1:length(n_vals)
    n = n_vals(i);
    
    % Numerical integration (manual trapezoidal rule)
    S_num(i) = CalVolume(a,b,n);
    
    % Analytical formula
    S_ana(i) = (4^(1-1/n)) * a * b * sqrt(pi) * gamma(1+1/n) / gamma(0.5+1/n);
end

% Plot comparison
figure;
plot(n_vals,S_num,'r-','LineWidth',2); hold on;
plot(n_vals,S_ana,'b--','LineWidth',2);
xlabel('n'); ylabel('Area S');
legend('Numerical','Analytical');
title('Superellipse Area vs n');
grid on;

% Percentage error
error_pct = 100*abs(S_num - S_ana)./S_ana;
figure;
plot(n_vals,error_pct,'m-o','LineWidth',2);
xlabel('n'); ylabel('Error (%)');
title('Relative Error between Numerical and Analytical');
grid on;

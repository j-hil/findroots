function [f4] = f4(x)
%f3 = (1/20)*(-x^3 + 8.5*x^2 + 8)
%   f3 is a function st f3(x)=x <=> F(x)=0 for CATAM question 5 called f(x)
%   throughout the report

f4 = x - (x.^3 - 8.5*x.^2 + 20*x - 8)./(3*x.^2 - 17*x + 20);
end

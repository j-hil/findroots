function [f3] = f3(x)
%f3 = (1/20)*(-x^3 + 8.5*x^2 + 8)
%   f3 is a function st f3(x)=x <=> F(x)=0 for CATAM question 5 called f(x)
%   throughout the report

f3 = x - (2*x - 3*sin(x) + 5)./(2 - 3*cos(x));
end

function [a] = bisectionF(x1,x2)
%Uses bisection method to find the root of F(x), outputs root and # of
%iterations used
%   Root must lie inbetween inputs

if F(x1)*F(x2) < 0 %checks inputs are ok, and determins the larger of the inputs
    if x1 > x2
        xh=x1;
        xl=x2;
    else
        xh=x2;
        xl=x1;
    end
elseif  F(x1)*F(x2) > 0
    disp('root not between inputs, try different inputs');
    return
elseif  F(x1)*F(x2) == 0
    disp('root is approximately one of your inputs')
    return
end

xn = (xh + xl)/2;
n=1;

while xh - xl > .5*10^(-5)
    
    t = F(xn);
    
    if t > 0
        xh=xn;
    elseif t < 0
        xl=xn;
    elseif t == 0
        disp('woah you got it baby! the root is')
        return
    end
    
    xn = (xh + xl)/2;
    n=n+1;
end

disp(['root is '  num2str(xn)  ' after '  num2str(n)  ' iterates.'])
a = [xn, n];
end


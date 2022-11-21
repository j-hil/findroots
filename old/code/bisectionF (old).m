xl = -pi;
xh = 0;
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
    end
    
    xn = (xh + xl)/2;
    n=n+1;
end

xn, n
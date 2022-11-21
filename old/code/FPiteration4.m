function [x] = FPiteration4(e, N, x0)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here


x1=0;
x2=x0;
n=0;

x=4;
fprintf(' $n$  & $x_n$      & $\\eps_n$   & $\\eps_{n+1}/\\eps_n$ \\\\ \\hline  \n')
fprintf('    0 & %10.6f & %10.6f & n/a        \\\\ \\hline  \n', x2, x2-x)

while abs(x2 - x1) > e && n < N
   
    err = x2 - x;
    x1=x2;
    x2=f4(x2);
    n=n+1;
    
    fprintf('%5.i & %10.6f & %10.6f & %10.6f \\\\ \\hline  \n', n, x2, x2-x, abs((x2 -x)/err))

end

x=x2;

end
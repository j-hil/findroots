function [x] = FPiteration2(e, N, x0)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here


x1=0;
x2=x0;
n=0;


while abs(x2 - x1) > e && n < N
   
    x1=x2;
    x2=f2(x2);
    n=n+1;
    

end

fprintf('x_N = %10.8f and N =%i \n',x2 , n )
x=x2;

end
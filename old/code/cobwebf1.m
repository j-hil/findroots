clf
a = linspace(-4.5,-0.5,1000);
hold on

x(1) = -2 ;
line([x(1),x(1)], [0,f2(x(1))]);
line([x(1),f1(x(1))], [f1(x(1)), f1(x(1))] )

for i=1:10
    x(i+1)=p(x(i));
    line([x(i+1),x(i+1)], [x(i+1),f1(x(i+1))]);
    line([x(i+1),f1(x(i+1))], [f1(x(i+1)), f1(x(i+1))]);
end

title(' ''Cobweb Diagram'' ')
xlabel('x')
ylabel('y')
grid on

h = plot(a,f1(a),a,a);
set(h(1),'LineStyle', '-', 'color', 'k')
set(h(2),'LineStyle', '--', 'color', 'k')
legend(h,' y = f(x)',' y = x')


 
 ax = gca;
 ax.XAxisLocation = 'bottom';
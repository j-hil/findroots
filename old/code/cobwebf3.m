clf
a = linspace(-22,0,1000);

hold on
x_0 = -1.3;
x_1 = f3(x_0);
x_2 = f3(x_1);

title(' Newton-Raphson ')
xlabel('x')
ylabel('y')
grid on

h = plot( ...
     a, F(a),...
     a, (2 - 3*cos(x_0))*(a-x_0) + F(x_0),...
     a, (2 - 3*cos(x_1))*(a-x_1) + F(x_1),...
     a, (2 - 3*cos(x_2))*(a-x_2) + F(x_2)...
        );

line([x_0 , x_0], [ 0 , F(x_0)], 'Color','k','LineStyle', '--');
line([x_1 , x_1], [ 0 , F(x_1)], 'Color','k','LineStyle', '--');
line([x_2 , x_2], [ 0 , F(x_2)], 'Color','k','LineStyle', '--');

set(h(1),'LineStyle', '-', 'color', 'b')   
set(h(2),'LineStyle', '-', 'color', 'k')
set(h(3),'LineStyle', '-', 'color', 'k')
set(h(4),'LineStyle', '-', 'color', 'k')

axis([-22, 0, -40,10])
legend(h,' y = F(x)', 'tangents')

ax = gca;
ax.XAxisLocation = 'origin';
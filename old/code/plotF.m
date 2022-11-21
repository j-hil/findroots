x = linspace(-4.5,-0.5,1000);
y = F(x);

plot(x,y)

title('y = F(x)')
xlabel('x')
ylabel('y')
grid on



ax = gca;
ax.XAxisLocation = 'origin';
seed = 124;
rns = RandStream('mt19937ar', 'seed', seed);

t = zeros(10,5);

for k = 1:10    
    
    i1 = 0;
    i2 = 0;
    
    while F(i1)*F(i2) > 0
        i1 = -13 + rand(rns)*20;
        i2 = -13 + rand(rns)*20;
    end
    
    a = bisectionF(i1,i2);
    t(k,:) = [i1, i2, a(1), a(2), abs(-2.88323687-a(1))];
    
    
end

%latex(vpa(sym(t),10))

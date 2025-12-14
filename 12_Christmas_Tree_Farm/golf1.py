print(sum('x'in l and 9*sum(map(int,(p:=l.split())[1:]))<=eval(p[0][:-1].replace('x','*'))for l in open(0)))

F,A=open(0).read().split("\n\n")
F=sorted([*map(int,x.split("-"))]for x in F.split())
S,E,C=*F.pop(0),0
for I in sorted(map(int,A.split())):
 while F and I>E:S,E=F.pop(0)
 C+=S<=I<=E
print(C)

F,A=open(0).read().split("\n\n")
C,F=0,sorted([*map(int,x.split("-"))]for x in F.split())
print(sum(any(a<=I<=b for a,b in F)for I in sorted(map(int,A.split()))))

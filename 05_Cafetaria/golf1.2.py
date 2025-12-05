F,A=open(0).read().split("\n\n")
C,G=0,[[*map(int,x.split("-"))]for x in F.split()]
print(sum(any(a<=I<=b for a,b in G)for I in map(int,A.split())))

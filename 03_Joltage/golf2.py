T=0
for I in open(0):
 P,k=I[:-1],11
 while~k:T+=int(C:=max(P[:len(P)-k]))*10**k;P=P[P.find(C)+1:];k-=1
print(T)

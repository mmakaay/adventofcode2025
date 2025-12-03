Z,P=0,50
for L in open(0):P,Z=(P+int(L[1:])*(1-2*(L[0]<'M')))%100,Z+(P<1)
print(Z)

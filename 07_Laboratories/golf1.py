T,r=0,open(0);d=next(r);b=[0]*len(d);b[d.find("S")]=1
for L in r:
 for i,c in enumerate(L):
  if c>"."and b[i]:b[i]=0;b[i-1]=b[i+1]=1;T+=1
print(T)

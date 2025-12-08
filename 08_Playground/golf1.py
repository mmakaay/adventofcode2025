import math
from collections import*
l,C,B,M=len(s:=[tuple(map(int,x.split(",")))for x in open(0)]),0,{},{}
for p in[(s[i],s[j])for i in range(l)for j in range(i+1,l)]:M[math.dist(*p)]=p
for i,d in enumerate(sorted(M)):
 if i>999:break
 a,b=M[d]
 if a in B and b in B:
  if B[a]!=B[b]:
   y=B[b]
   for n,c in B.items():
    if c==y:B[n]=B[a]
 elif a in B:B[b]=B[a]
 elif b in B:B[a]=B[b]
 else:C+=1;B[a]=B[b]=C
S=sorted(Counter(B.values()).values())
print(S[-1]*S[-2]*S[-3])

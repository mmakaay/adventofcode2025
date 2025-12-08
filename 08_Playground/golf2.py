import math
l,B=len(s:=[eval(x)for x in open(0)]),{}
for _,a,b in sorted((math.dist(s[i],s[j]),s[i],s[j])for i in range(l)for j in range(i+1,l)):
 x,y=B.get(a,a),B.get(b,b);B={n:[B[n],x][B[n]==y]for n in B};B[a]=B[b]=x
 if len(B)==l and len({*B.values()})<2:print(a[0]*b[0]);break

import math,collections
l,B=len(s:=[eval(x)for x in open(0)]),{}
for _,a,b in sorted((math.dist(s[i],s[j]),s[i],s[j])for i in range(l)for j in range(i+1,l))[:1000]:
 x,y=B.get(a,a),B.get(b,b);B={n:[B[n],x][B[n]==y]for n in B};B[a]=B[b]=x
a,b,c=sorted(collections.Counter(B.values()).values())[-3:];print(a*b*c)

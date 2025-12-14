m,n,T=min,max,[list(map(int,k.split(",")))for k in open(0)]
E=list(zip(T,T[1:]+T[:1]))
b,a=[((m(u,w),n(v,x)),(n(u,w),m(v,x)))for(u,v),(w,x)in E if abs(u-w)>9999]
def L(u,v,d):
 o,y=u;A,p=0,v[0]
 for(g,h),(i,j)in E:
  if h==j and m(g,i)<=p<=n(g,i)and(h-y)*d>0:Y=h;break
 for e,f in T:
  if o>e>p or y<f<Y or y>f>Y:continue
  if any(h==j and m(y,f)<h<n(y,f)and m(g,i)<=p and n(g,i)>=e for(g,h),(i,j)in E):continue
  A=n(A,(p-e+1)*(abs(f-y)+1))
 return A
print(n(L(*a,1),L(*b,-1)))

m,n,R,T=min,max,[tuple(map(int,line.split(",")))for line in open(0)],0
def z(u,v,w,x):return((m(u,w),n(v,x)),(n(u,w),m(v,x)))
E=[z(*p,*q)for p,q in sorted(zip(R,R[1:]+R[:1]))]
for(X,M),(A,S)in[z(*p1,*p2)for p1 in R for p2 in R]:
 if(O:=(abs(A-X)+1)*(abs(S-M)+1))>T:T=[O,T][any([(S<c<M)+(b>X)+(a<A)>2,(X<a<A)+(d>S)+(c<M)>2][a==b]for(a,c),(b,d)in E)]
print(T)

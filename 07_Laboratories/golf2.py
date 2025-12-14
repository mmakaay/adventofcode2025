import functools as f
l=tuple(open(0));w=len(l[0])-1
@f.cache
def B(x,y=len(l)-1):y-=1;u=l[y];return(u[x]=="S")+B(x-1,y)*(u[x-1]>"S")+B(x,y)*(u[x]<"S")+(B(x+1,y)if u[x+1]>"S"else 0)if~y else 0
print(sum(map(B,range(w))))

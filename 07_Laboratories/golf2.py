import functools as f
l=tuple(open(0));w=len(l[0])-1
@f.cache
def B(x,y=len(l)-1,r=0):
 if y:y-=1;r=(l[y][x]=="S")+B(x-1,y)*(l[y][x-1]>"S")+B(x,y)*(l[y][x]<"S")+(B(x+1,y) if l[y][x+1]>"S" else 0)
 return r
print(sum(map(B,range(w))))

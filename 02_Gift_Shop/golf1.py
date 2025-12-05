import re
T=0
for a,b in[tuple(map(int,r.split("-")))for r in next(open(0)).split(",")]:
 while a<=b:
  if re.match(r"^(\d+)\1$",str(a)):T+=a
  a+=1
print(T)

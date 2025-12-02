#!/usr/bin/env python3
import re;import sys;T=0
for a,b in[tuple(map(int,r.split("-")))for r in next(sys.stdin).split(",")]:
 while a<=b:
  if re.match(r"^(\d+)\1+$",str(a)):T+=a
  a+=1
print(T)


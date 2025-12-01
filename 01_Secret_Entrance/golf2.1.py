#!/usr/bin/env python3
import sys;Z,P=0,50
for L in sys.stdin:
 D,A=L[0]<'M',int(L[1:])
 while A:T=min([100-P,P][D]or 100,A);P,A,Z=(P+(1-2*D)*T)%100,A-T,Z+(P<1)
print(Z)

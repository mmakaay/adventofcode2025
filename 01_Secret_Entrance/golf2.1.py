#!/usr/bin/env python3
import sys;Z,P=0,50
for L in sys.stdin:
 for _ in range(int(L[1:])):Z+=(P:=(P+1-2*(L[0]<'M'))%100)<1
print(Z)


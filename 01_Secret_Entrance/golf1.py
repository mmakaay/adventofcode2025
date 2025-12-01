#!/usr/bin/env python3
import sys;Z,P=0,50
for L in sys.stdin:P,Z=(P+int(L[1:])*(1-2*(L[0]<'M')))%100,Z+(P<1)
print(Z)

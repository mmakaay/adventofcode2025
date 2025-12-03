#!/usr/bin/python3
import sys;T=0
for I in sys.stdin:
 P=str(int(I))
 for k in[2,1]:T+=int(C:=max(A:=P[:len(P)-k+1]))*10**(k-1);P=P[A.index(C)+1:]
print(T)

#!/usr/bin/python3
import sys;T=0
for P in sys.stdin:
 k,P=13,str(int(P))
 while k:=k-1:T+=int(C:=max(A:=P[:len(P)-k+1]))*10**(k-1);P=P[A.index(C)+1:]
print(T)

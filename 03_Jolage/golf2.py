#!/usr/bin/env python3
import sys;T=0
for P in map(str.strip,sys.stdin):
 B,k="",13
 while k:=k-1:B+=(C:=max(A:=P[:len(P)-k+1]));P=P[A.index(C)+1:]
 T+=int(B)
print(T)

G,C=sorted([*map(int,x.split("-"))]for x in open(0).read().split("\n\n")[0].split()),0
while G:
 s,e=G.pop(0)
 while G and s<=G[0][0]<=e:g,h=G.pop(0);e=max(e,h)
 C+=e-s+1
print(C)

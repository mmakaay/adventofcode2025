G={l[:3]:l[5:-1].split()for l in open(0)}
def F(n):return 1 if n=="out"else sum(F(n)for n in G[n])
print(F("you"))

#!/usr/bin/env python3

import sys

data = sys.stdin.read()
fresh, available = data.split("\n\n") 
fresh = sorted(tuple(map(int, x.split("-"))) for x in fresh.split())
available = sorted(map(int, available.split()))

count = 0
bucket_start, bucket_end = fresh.pop(0)

for ingredient in available:
    while fresh and ingredient > bucket_end:
        bucket_start, bucket_end = fresh.pop(0)
    if bucket_start <= ingredient <= bucket_end:
        count += 1
        
print(count)


N = int(input())
A = list(map(int, input().split()))
num = [A.count(i) for i in range(1,5)]
B = []
for i in range(4):
    B += [i+1]*num[i]

G = [[0]*4 for _ in range(4)]
nn = 1
for i in range(N):
    if A[i]!=B[i]:
        G[A[i]-1][B[i]-1] += 1

from itertools import permutations

res = 0
for v in permutations(range(4),2):
    nm = float('inf')
    for i in range(len(v)):
        nm = min(nm,G[v[i]][v[(i+1)%len(v)]])
    res += nm
    for i in range(len(v)):
        G[v[i]][v[(i+1)%len(v)]] -= nm

for v in permutations(range(4),3):
    nm = float('inf')
    for i in range(len(v)):
        nm = min(nm,G[v[i]][v[(i+1)%len(v)]])
    res += 2*nm
    for i in range(len(v)):
        G[v[i]][v[(i+1)%len(v)]] -= nm   

for v in permutations(range(4),4):
    nm = float('inf')
    for i in range(len(v)):
        nm = min(nm,G[v[i]][v[(i+1)%len(v)]])
    res += 3*nm
    for i in range(len(v)):
        G[v[i]][v[(i+1)%len(v)]] -= nm  
print(res)

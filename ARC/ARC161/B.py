from itertools import combinations
from bisect import bisect_right as br

num = []
p = [1<<i for i in range(60)]
for v in combinations(range(60),3):
    num.append(p[v[0]]+p[v[1]]+p[v[2]])
num.sort()

T = int(input())
for i in range(T):
    n = int(input())
    idx = br(num,n)
    if idx==0:
        print(-1)
    else:
        print(num[idx-1])

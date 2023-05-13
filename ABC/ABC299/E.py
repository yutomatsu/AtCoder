from collections import deque

N, M = map(int, input().split())
G = [list() for _ in range(N)]
for i in range(M):
    u,v = map(int, input().split())
    u-=1;v-=1
    G[u].append(v)
    G[v].append(u)

cnt = [list() for _ in range(N)]
bad = [0]*N
dq = deque()
K = int(input())
for i in range(K):
    p,d = map(int, input().split())
    p-=1
    if d==0:
        cnt[p].append(p)
        continue
    bad[p] = 1
    dis = [-1]*N
    dis[p] = 0
    dq.append(p)
    while dq:
        v = dq.popleft()
        for nex in G[v]:
            if dis[nex]==-1 and dis[v]<d:
                dis[nex] = dis[v]+1
                if dis[nex]<d:
                    bad[nex] = 1
                    dq.append(nex)
                elif dis[nex]==d:
                    cnt[nex].append(p)

seen = set()
ans = ['0']*N
for i in range(N):
    if bad[i]==0:
        ans[i] = '1'
        for v in cnt[i]:
            seen.add(v)
if len(seen)==K:
    print('Yes')
    print(''.join(ans))
else:
    print('No')

import sys
input = sys.stdin.readline
from heapq import heappush, heappop
INF = float('inf')

def dijkstra(s, n):
    dist = [INF] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        dis, v = heappop(hq)
        if dist[v] < dis:
            continue
        seen[v] = True
        for to, cost in G[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist[-1]

N, M = map(int, input().split())
size = [0]*N
S = []
num = [0]*M
for i in range(N):
    size[i] = int(input())
    s = list(map(int, input().split()))
    for j in range(size[i]):
        num[s[j]-1] += 1
    S.append(s)

sm = [0]*(M+1)
for i in range(M):
    sm[i+1] = sm[i]+num[i]
G = [list() for _ in range(sm[-1]+M+2)]
id = [0]*M
idx = [list() for _ in range(M)]
for s in S:
    for i in range(len(s)-1):
        id_from = sm[s[i]-1]+id[s[i]-1]
        id_to = sm[s[i+1]-1]+id[s[i+1]-1]
        idx[s[i]-1].append(id_from)
        G[id_from].append((id_to,0))
        G[id_to].append((id_from,0))
        id[s[i]-1] += 1
        if i==len(s)-2:
            idx[s[i+1]-1].append(id_to)
            id[s[i+1]-1] += 1

for i in range(M):
    for j in range(len(idx[i])):
        id_from,id_to = idx[i][j],sm[-1]+i
        G[id_from].append((id_to,0))
        G[id_to].append((id_from,1))

for i in range(len(idx[0])):
    G[sm[-1]+M].append((idx[0][i],0))
for i in range(len(idx[-1])):
    G[idx[-1][i]].append((sm[-1]+M+1,0))

res = dijkstra(sm[-1]+M,sm[-1]+M+2)
print(res if res!=INF else -1)
    

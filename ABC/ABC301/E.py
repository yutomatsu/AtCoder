from collections import deque

H, W, T = map(int,input().split())
A = [input() for _ in range(H)]

kasi = []
for i in range(H):
    for j in range(W):
        if A[i][j]=='S':
            sx,sy = i,j
        if A[i][j]=='G':
            gx,gy = i,j
        if A[i][j]=='o':
            kasi.append((i,j))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    d = deque()
    dis = [[float('inf')]*W for _ in range(H)]
    dis[i][j] = 0
    d.append((i,j))
    while d:
        x,y = d.popleft()
        for k in range(4):
            cx = x+dx[k]
            cy = y+dy[k]
            if 0<=cx<H and 0<=cy<W and A[cx][cy]!='#' and dis[cx][cy]==float('inf'):
                dis[cx][cy] = dis[x][y]+1
                d.append((cx,cy))
    return dis

dis_s = bfs(sx,sy)
dis_g = bfs(gx,gy)

dis_kasi = []
for x,y in kasi:
    dis_kasi.append(bfs(x,y))

l = len(kasi)
dp = [[float('inf')]*l for _ in range(1<<l)]
for i in range(l):
    dp[1<<i][i] = dis_kasi[i][sx][sy]

for i in range(1<<l):
    for j in range(l):
        if i&(1<<j):
            for k in range(l):
                if not i&(1<<k):
                    x1,y1 = kasi[j]
                    x2,y2 = kasi[k]
                    dp[i^(1<<k)][k] = min(dp[i^(1<<k)][k],dp[i][j]+dis_kasi[j][x2][y2])

res = 0 if dis_s[gx][gy]<=T else -1
for i in range(1<<l):
    cnt = 0
    for j in range(l):
        if i&(1<<j):
            cnt += 1
    for j in range(l):
        x,y = kasi[j]
        if dp[i][j]+dis_g[x][y]<=T:
            res = max(res,cnt)
print(res)

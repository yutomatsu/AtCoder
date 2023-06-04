T = int(input())

def solve(N,G,S):
    ans = ['-']*N
    p = [-1]*N
    stack = [(0,1)]
    while stack:
        v,t = stack.pop()
        if t==1:
            stack.append((v,-1))
            for nex in G[v]:
                if p[v]==nex:continue
                p[nex] = v
                stack.append((nex,1))
        else:
            b,w = 0,0
            for nex in G[v]:
                if p[v]==nex:
                    continue
                if ans[nex]=='B':
                    b += 1
                else:
                    w += 1
            if ans[v]=='-':
                ans[v] = S[p[v]]
            if S[v]=='B':
                if b==w:
                    if ans[p[v]]!='W':
                        ans[p[v]] = 'B'
                    else:
                        return -1
                elif w>b:
                    return -1
            else:
                if b==w:
                    if ans[p[v]]!='B':
                        ans[p[v]] = 'W'
                    else:
                        return -1
                elif b>w:
                    return -1
    for i in range(N):
        b,w = 0,0
        for nex in G[i]:
            assert ans[nex]=='B' or ans[nex]=='W'
            if ans[nex]=='B':
                b += 1
            else:
                w += 1
        if b>w:
            assert S[i]=='B'
        if w>b:
            assert S[i]=='W'
    return ''.join(ans)



for i in range(T):
    N = int(input())
    G = [list() for _ in range(N)]
    for i in range(N-1):
        a,b = map(int, input().split())
        a-=1;b-=1
        G[a].append(b)
        G[b].append(a)
    S = input()
    print(solve(N,G,S))

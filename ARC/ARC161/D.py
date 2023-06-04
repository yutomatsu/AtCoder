N,D = map(int,input().split())

if N*(N-1)//2<D*N:
    print('No')
    exit()

edge = []
seen = set()
for i in range(N):
    edge.append([i+1,(i+1)%N+1])
    seen.add((i+1,(i+1)%N+1))

iter = [i for i in range(N)]
iter = iter[::-1]
iter.pop()
num = D*N-N
v = 0
while num:
    for j in iter:
        if (v+1,j+1) not in seen and (j+1,v+1) not in seen:
            edge.append([v+1,j+1])
            seen.add((v+1,j+1))
            num -= 1
            if num==0:
                break
    if iter:
        iter.pop()
        v += 1
print('Yes')
for a,b in edge:
    print(a,b)

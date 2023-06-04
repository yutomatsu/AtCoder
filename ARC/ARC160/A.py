N, K = map(int, input().split())
A = list(map(int, input().split()))

idx = [-1]*N
for i in range(N):
    idx[A[i]-1] = i

B = []
seen = set()
for i in range(N):
    num = 1
    while K:
        if num in seen:
            num += 1
            continue
        if num==A[i]:
            cnt = N+(N-i-1)*(N-i-2)//2
        else:
            cnt = 1
        if K>cnt:
            K -= cnt
        else:
            break
        num += 1
    if num!=A[i]:
        B = B+A[i:idx[num-1]+1][::-1]+A[idx[num-1]+1:]
        break
    else:
        B.append(num)
        seen.add(num)
print(*B)

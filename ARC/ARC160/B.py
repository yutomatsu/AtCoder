T = int(input())
mod = 998244353
for i in range(T):
    N = int(input())
    res = 0
    for i in range(1,N+1):
        if i*i>N:
            break
        res += 1
    for i in range(1,N+1):
        if i*i>N:
            break
        res += 3*(N//i)
        if N//i>=i:
            res -= 3
        res %= mod
    for y in range(1,N+1):
        if y*y>N:break
        res += 6*(y-1)*(N//y-y)
        res %= mod
    print(res)

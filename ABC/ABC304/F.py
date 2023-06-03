N = int(input())
S = input()
m = []
for i in range(N):
    if S[i]=='.':
        m.append(i)

mod = 998244353
ans = [0]*N
res = 0
for i in range(1,N):
    if N%i==0:
        s = set()
        for mm in m:
            s.add(mm%i)
        ans[i] += pow(2,i-len(s),mod)
        for k in range(2*i,N,i):
            ans[k] -= ans[i]
            ans[k] %= mod
        res += ans[i]
        res %= mod
print(res)

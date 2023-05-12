N = int(input())

num = [0,0,0]
while N%2==0:
    N //= 2
    num[0] += 1
while N%3==0:
    N //= 3
    num[1] += 1
while N%5==0:
    N //= 5
    num[2] += 1

if N!=1:
    print(0)
    exit()

res = 0
mod = 998244353
fac = [0]*10**6
inv = [0]*10**6
nv = pow(5,mod-2,mod)
fac[0]=inv[0]=1
for i in range(1,10**6):
    fac[i] = (fac[i-1]*i)%mod
    inv[i] = (inv[i-1]*pow(i,mod-2,mod))%mod

res = 0
for i in range(100):
    for j in range(100):
        if i*2+j>num[0] or j>num[1]:continue
        nn = [0,num[0]-2*i-j,num[1]-j,i,num[2],j]
        sm = sum(nn)
        res += (fac[sm]*inv[nn[1]]*inv[nn[2]]*inv[nn[3]]*inv[nn[4]]*inv[nn[5]]*pow(nv,sm,mod))%mod
        res %= mod
print(res)

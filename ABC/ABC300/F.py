N,M,K = map(int, input().split())
S = input()

n1,n2 = 0,0
for i in range(N):
    if S[i]=='x':
        n1 = i
        break
for i in range(N):
    if S[-1-i]=='x':
        n2 = i
        break

x = S.count('x')
res = 0
a,b = K//x,K%x
S2 = S+S
S3 = S2+S

def syaku(A,L,B,f=False):
    l,r = 0,0
    cnt,sm = 0,0
    while l<L:
        while r<L and cnt<=B:
            if A[r]=='o':
                r += 1
            else:
                if cnt<B:
                    cnt += 1
                    r += 1
                else:
                    break
        sm = max(sm,r-l)
        if A[l]=='x':
            cnt -= 1
        l += 1
    return sm

if M==1:
    if a==0:
        print(syaku(S,N,b))
    else:
        print(N)
else:
    if a==0:
        print(syaku(S2,2*N,b))
    else:
        if M==a:
            print(N*M)
        elif M==a+1:
            print(N*(a-1)+syaku(S2,2*N,b+x))
        else:
            print(N*(a-1)+syaku(S3,3*N,b+x))

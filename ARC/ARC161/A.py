N = int(input())
A = list(map(int, input().split()))

A.sort()
B = [0]*N
id = 0
for i in range(0,N,2):
    B[i] = A[id]
    id += 1

for i in range(1,N,2):
    B[i] = A[id]
    id += 1

for i in range(1,N,2):
    if B[i-1]>=B[i] or B[i]<=B[i+1]:
        print('No')
        exit()
print('Yes')

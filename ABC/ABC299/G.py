class SegmentTree():
    """UnitXは単位元、fは区間で行いたい操作、initは自然数あるいは配列"""
    def __init__(self, init, unitX, f):
        self.f = f # (X, X) -> X
        self.unitX = unitX
        self.f = f
        if type(init) == int:
            self.n = init
            self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * (self.n * 2)
        else:
            self.n = len(init)
            self.n = 1 << (self.n - 1).bit_length()
            # len(init)が2の累乗ではない時UnitXで埋める
            self.X = [unitX] * self.n + init + [unitX] * (self.n - len(init))
            # 配列のindex1まで埋める
            for i in range(self.n-1, 0, -1):
                self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
    
    def update(self, i, x):
        """0-indexedのi番目の値をxで置換"""
        # 最下段に移動
        i += self.n
        self.X[i] = x
        # 上向に更新
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
            i >>= 1
    
    def getvalue(self, i):
        """元の配列のindexの値を見る"""
        return self.X[i + self.n]
    
    def getrange(self, l, r):
        """区間[l, r)でのfを行った値"""
        l += self.n
        r += self.n
        al = self.unitX
        ar = self.unitX
        while l < r:
            # 左端が右子ノードであれば
            if l & 1:
                al = self.f(al, self.X[l])
                l += 1
            # 右端が右子ノードであれば
            if r & 1:
                r -= 1
                ar = self.f(self.X[r], ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)

def op(a,b):
    if a[0]<b[0]:
        return a
    elif a[0]>b[0]:
        return b
    else:
        return (a[0],min(a[1],b[1]))

N, M = map(int, input().split())
A = list(map(int, input().split()))

idx = [list() for _ in range(M)]
for i in range(N):
    idx[A[i]-1].append(i)

B = [idx[i][-1] for i in range(M)]
suf = SegmentTree(B,float('inf'),min)
st = SegmentTree([[a,i] for i,a in enumerate(A)],[float('inf'),float('inf')],op)
posi = 0
res = []
while len(res)<M:
    s = suf.getrange(0,len(B))
    mn,id = st.getrange(posi,s+1)
    res.append(mn)
    posi = id+1
    suf.update(mn-1,float('inf'))
    for nn in idx[mn-1]:
        st.update(nn,(float('inf'),nn))
print(*res)

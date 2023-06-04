from collections import defaultdict
from random import randint

from typing import List

class UnionFind:
    """0-indexed"""
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        self.__group_count = n

    def unite(self, x, y) -> bool:
        """xとyをマージ"""
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False

        self.__group_count -= 1

        if self.parent[x] > self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True

    def is_same(self, x, y) -> bool:
        """xとyが同じ連結成分か判定"""
        return self.root(x) == self.root(y)

    def root(self, x) -> int:
        """xの根を取得"""
        if self.parent[x] < 0:
            return x
        else:
            # 経路圧縮あり
            # self.parent[x] = self.root(self.parent[x])
            # return self.parent[x]
            # 経路圧縮なし
            return self.root(self.parent[x])

    def size(self, x) -> int:
        """xが属する連結成分のサイズを取得"""
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        """全連結成分のサイズのリストを取得 O(N)"""
        sizes = []
        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes
    
    def members(self, x, y) -> List[int]:
        mem_x = []
        mem_y = []
        rx = self.root(x)
        ry = self.root(y)
        for i in range(self.n):
            r = self.root(i)
            if r == rx:
                mem_x.append(i)
            if r==ry:
                mem_y.append(i)
        return mem_x,mem_y

    def groups(self) -> List[List[int]]:
        """全連結成分の内容のリストを取得 O(N・α(N))"""
        groups = dict()
        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)
        return list(groups.values())

    @property
    def group_count(self) -> int:
        """連結成分の数を取得 O(1)"""
        return self.__group_count

def destruct(y,x):
    """マス(y,x)を掘削"""
    if destructed[y][x]:
        return True
    destructed[y][x] = True

    res = 0
    power = init_power[C]
    while res==0:
        assert 1<=power<=5000
        assert 0<=x<200
        assert 0<=y<200

        if sub:
            print(y,x,power)
            res = int(input())
        else:
            # local
            global score
            score += power+C
            res = judge(y,x,power)
            if res==-1:
                print(f'({y}, {x}) already destructed')
                exit()
            with open('output.txt',mode='a') as f:
                f.write('{} {} {}\n'.format(y,x,power))

        power *= 2
        if power>limit_power[C]:
            power = init_power[C]
    if res == 1:
        return True
    else:
        return False

def try_destruct(y,x):
    if destructed[y][x]:
        return True
    assert 0<=x<200
    assert 0<=y<200
    if sub:
        print(y,x,greed_power)
        res = int(input())
    else:
        # local
        global score
        score += greed_power+C
        res = judge(y,x,greed_power)
        if res==-1:
            print(f'({y}, {x}) already destructed (try)')
            exit()
        with open('output.txt',mode='a') as f:
            f.write('{} {} {}\n'.format(y,x,greed_power))

    if res==2 or res==-1:
        exit()
    if res==1:
        return True
    else:
        return False

def judge(y,x,P):
    if S[y][x]<=0:
        return -1
    S[y][x] -= P
    if S[y][x]<=0:
        return 1
    else:
        return 0

def move_randam(y1,x1,y2,x2):
    f = destruct(y1,x1)
    if not f:exit()
    f = destruct(y2,x2)
    if not f:exit()
    posi_y, posi_x = y1,x1
    bf_posi_y,bf_posi_x = posi_y, posi_x
    while posi_y!=y2 or posi_x!=x2:
        if posi_y==y2:
            if posi_x<x2:
                posi_x += 1
            else:
                posi_x -= 1
        elif posi_x==x2:
            if posi_y<y2:
                posi_y += 1
            else:
                posi_y -= 1
        else:
            rand = randint(1,1<<60)
            if rand&1:
                if posi_y<y2:
                    posi_y += 1
                else:
                    posi_y -= 1
            else:
                if posi_x<x2:
                    posi_x += 1
                else:
                    posi_x -= 1
        f = destruct(posi_y,posi_x)
        if not f:exit()
        new_uf.unite(bf_posi_y*N+bf_posi_x,posi_y*N+posi_x)
        if new_uf.is_same(y1*N+x1,y2*N+x2):
            return 
        bf_posi_y,bf_posi_x = posi_y,posi_x
    print('connection ok')
    assert posi_y==y2 and posi_x==x2
    assert new_uf.is_same(y1*N+x1,y2*N+x2)
    return

def connect_new(y1,x1,y2,x2,cnt):
    f = destruct(y1,x1)
    if not f:exit()
    f = destruct(y2,x2)
    if not f:exit()
    posi_y,posi_x = y1,x1
    opt_flag = True
    if y1==y2 or x1==x2:
        opt_flag = False
    while posi_y!=y2 or posi_x!=x2:
        if opt_flag:
            if posi_y<y2:
                flag1 = try_destruct(posi_y+1,posi_x)
                if flag1:
                    destructed[posi_y+1][posi_x] = True
                    new_uf.unite(posi_y*N+posi_x,(posi_y+1)*N+posi_x)
            else:
                flag1 = try_destruct(posi_y-1,posi_x)
                if flag1:
                    destructed[posi_y-1][posi_x] = True
                    new_uf.unite(posi_y*N+posi_x,(posi_y-1)*N+posi_x)
            if posi_x<x2:
                flag2 = try_destruct(posi_y,posi_x+1)
                if flag2:
                    destructed[posi_y][posi_x+1] = True
                    new_uf.unite(posi_y*N+posi_x,posi_y*N+posi_x+1)
            else:
                flag2 = try_destruct(posi_y,posi_x-1)
                if flag2:
                    destructed[posi_y][posi_x-1] = True
                    new_uf.unite(posi_y*N+posi_x,posi_y*N+posi_x-1)
            if not flag1 and not flag2:
                if cnt==1:
                    connect_new(y2,x2,posi_y,posi_x,2)
                    return
                else:
                    move_randam(posi_y,posi_x,y2,x2)
                    return
            elif flag1 and flag2:
                bf_posi_y,bf_posi_x = posi_y,posi_x
                diff_y = abs(y2-posi_y)
                diff_x = abs(x2-posi_x)
                if diff_y>=diff_x:
                    if posi_y<y2:
                        posi_y += 1
                    else:
                        posi_y -= 1
                else:
                    if posi_x<x2:
                        posi_x += 1
                    else:
                        posi_x -= 1
                if posi_y==y2 or posi_x==x2:
                    opt_flag = False
                new_uf.unite(bf_posi_y*N+bf_posi_x,posi_y*N+posi_x)
                if new_uf.is_same(y1*N+x1,y2*N+x2):
                    return
            elif flag1:
                bf_posi_y,bf_posi_x = posi_y,posi_x
                if posi_y<y2:
                    posi_y += 1
                else:
                    posi_y -= 1
                if posi_y==y2 or posi_x==x2:
                    opt_flag = False
                new_uf.unite(bf_posi_y*N+bf_posi_x,posi_y*N+posi_x)
                if new_uf.is_same(y1*N+x1,y2*N+x2):
                    return
            else:
                bf_posi_y,bf_posi_x = posi_y,posi_x
                if posi_x<x2:
                    posi_x += 1
                else:
                    posi_x -= 1
                if posi_y==y2 or posi_x==x2:
                    opt_flag = False
                new_uf.unite(bf_posi_y*N+bf_posi_x,posi_y*N+posi_x)
                if new_uf.is_same(y1*N+x1,y2*N+x2):
                    return
        else:
            if cnt==1:
                connect_new(y2,x2,posi_y,posi_x,2)
                return
            else:
                move_randam(posi_y,posi_x,y2,x2)
                return
    return

def dist(id1,id2):
    if id1<K:
        y1,x1 = house_posi[id1]
    else:
        y1,x1 = water_posi[id1-K]
    if id2<K:
        y2,x2 = house_posi[id2]
    else:
        y2,x2 = water_posi[id2-K]
    return abs(x1-x2)+abs(y1-y2)


####################
sub = True
####################

N, W, K, C = map(int, input().split())

if not sub:
    S = [list(map(int, input().split())) for _ in range(N)]

water_posi = [list(map(int,input().split())) for _ in range(W)]
house_posi = [list(map(int,input().split())) for _ in range(K)]

init_power = {1:10,2:12,4:15,8:20,16:30,32:50,64:70,128:100}
limit_power = {1:90,2:180,4:225,8:300,16:450,32:750,64:1050,128:1500}
greed_power = 35

score = 0

cost = [[0]*N for _ in range(N)]
destructed = [[False]*N for _ in range(N)]
for y,x in house_posi:
    f = destruct(y,x)
    if not f:exit()

edge = []
uf = UnionFind(K+W)
for i in range(K+W):
    for j in range(i+1,K+W):
        edge.append([dist(i,j),i,j])
edge.sort()

TF = defaultdict(int)
for i in range(W):
    TF[uf.root(i+K)] = 1
select_edge = []
for _,a,b in edge:
    if uf.is_same(a,b):continue
    f1,f2 = TF[uf.root(a)],TF[uf.root(b)]
    if f1 and f2:continue
    if f1 or f2:
        uf.unite(a,b)
        TF[uf.root(a)] = 1
    else:
        uf.unite(a,b)
        rand = randint(1,1<<60)
        if rand&1:
            a,b = b,a
    select_edge.append([a,b])
    
new_uf = UnionFind(N*N)
for a, b in select_edge:
    if a>=K:
        y1,x1 = water_posi[a-K]
    else:
        y1,x1 = house_posi[a]
    if b>=K:
        y2,x2 = water_posi[b-K]
    else:
        y2,x2 = house_posi[b]

    mem_a, mem_b = new_uf.members(y1*N+x1,y2*N+x2)
    distance = float('inf')
    for P in mem_a:
        y1,x1 = P//N,P%N
        for Q in mem_b:
            y2,x2 = Q//N,Q%N
            if distance>abs(y1-y2)+abs(x1-x2):
                distance = abs(y1-y2)+abs(x1-x2)
                res_y1,res_x1,res_y2,res_x2 = y1,x1,y2,x2
    connect_new(res_y1,res_x1,res_y2,res_x2,1)

    # print(y1,x1,y2,x2)
    # connect_new(y1,x1,y2,x2,1)

HOUSE = [new_uf.root(i*N+j) for i,j in house_posi]
WATER = set([new_uf.root(i*N+j) for i, j in water_posi])
for root in HOUSE:
    assert root in WATER

if not sub:
    print(score)

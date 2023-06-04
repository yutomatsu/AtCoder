from collections import deque

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def match(s):
    d = deque()
    seen = [[[-1]*D for _ in range(D)] for _ in range(D)]
    for xx,yy,zz in s:
        seen[xx][yy][zz] = 0
    cnt = 1
    block_num = []
    num = 0
    for x,y,z in s:
        if seen[x][y][z]>0:continue
        d.append((x,y,z))
        seen[x][y][z] = cnt
        num += 1
        while d:
            xx,yy,zz = d.popleft()
            for i in range(6):
                cx = xx+dx[i]
                cy = yy+dy[i]
                cz = zz+dz[i]
                if 0<=cx<D and 0<=cy<D and 0<=cz<D and seen[cx][cy][cz]==0:
                    seen[cx][cy][cz] = seen[x][y][z]
                    d.append((cx,cy,cz))
                    num += 1
        cnt += 1
        block_num.append(num)
        num = 0
    return seen,block_num

def delete(x,y,z,i):
    if i==1:
        for xx in range(D):
            for yy in range(D):
                if xx==x or yy==y:continue
                if (xx,y,z) in block1 and (x,yy,z) in block1:
                    return True
        return False
    else:
        for xx in range(D):
            for yy in range(D):
                if xx==x or yy==y:continue
                if (xx,y,z) in block2 and (x,yy,z) in block2:
                    return True
        return False

D = int(input())
wx,wy,wz = D*D,D,1
front1 = [input() for _ in range(D)]
right1 = [input() for _ in range(D)]
front2 = [input() for _ in range(D)]
right2 = [input() for _ in range(D)]

block1 = set()
block2 = set()
for x in range(D):
    for y in range(D):
        for z in range(D):
            if front1[z][x]=='1' and right1[z][y]=='1':
                block1.add((x,y,z))
            if front2[z][x]=='1' and right2[z][y]=='1':
                block2.add((x,y,z))

MAX = 0
ans = []
ans_block = []
rot = [[1,2,3],[-2,1,3],[-1,-2,3],[2,-1,3]]
id = -1
s = []
for x in range(D):
    for y in range(D):
        for z in range(D):
            if (x,y,z) in block1 and (x,y,z) in block2:
                s.append((x,y,z))
            
seen,block_num = match(s)
res = sum([i for i in block_num if i>1])
if MAX<res:
    ans = seen
    id = 0
    MAX = res
    ans_block = block_num

s = []
for x in range(D):
    for y in range(D):
        for z in range(D):
            if (x,y,z) in block1 and (D-1-y,x,z) in block2:
                s.append((x,y,z))
            
seen,block_num = match(s)
res = sum([i for i in block_num if i>1])
if MAX<res:
    ans = seen
    id = 1
    MAX = res
    ans_block = block_num

s = []
for x in range(D):
    for y in range(D):
        for z in range(D):
            if (x,y,z) in block1 and (D-1-x,D-1-y,z) in block2:
                s.append((x,y,z))
            
seen,block_num = match(s)
res = sum([i for i in block_num if i>1])
if MAX<res:
    ans = seen
    id = 2
    MAX = res
    ans_block = block_num

s = []
for x in range(D):
    for y in range(D):
        for z in range(D):
            if (x,y,z) in block1 and (y,D-1-x,z) in block2:
                s.append((x,y,z))
            
seen,block_num = match(s)
res = sum([i for i in block_num if i>1])
if MAX<res:
    ans = seen
    id = 3
    MAX = res
    ans_block = block_num

if len(ans)==0:
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if (x,y,z) in block1:
                    if delete(x,y,z,1):
                        block1.remove((x,y,z))
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if (x,y,z) in block2:
                    if delete(x,y,z,2):
                        block2.remove((x,y,z))
    c1,c2 = 1,1
    res1 = [0]*(D**3)
    res2 = [0]*(D**3)
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if (x,y,z) in block1:
                    res1[x*wx+y*wy+z*wz] = c1
                    c1 += 1
                if (x,y,z) in block2:
                    res2[x*wx+y*wy+z*wz] = c2
                    c2 += 1
    print(max(c1,c2)-1)
    print(*res1)
    print(*res2)
else:
    use = set([id+1 for id,i in enumerate(ans_block) if i>1])
    col = {}
    color = 1
    for bb in use:
        col[bb] = color
        color += 1
    res1 = [0]*D**3
    res2 = [0]*D**3
    cnt = len(use)
    used1 = set()
    used2 = set()
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if ans[x][y][z]>0 and ans[x][y][z] in use:
                    C = col[ans[x][y][z]]
                    res1[x*wx+y*wy+z*wz] = C
                    used1.add((x,y,z))
                    if id==0:
                        res2[x*wx+y*wy+z*wz] = C
                        used2.add((x,y,z))
                    elif id==1:
                        res2[(D-1-y)*wx+x*wy+z*wz] = C
                        used2.add((D-1-y,x,z))
                    elif id==2:
                        res2[(D-1-x)*wx+(D-1-y)*wy+z*wz] = C
                        used2.add((D-1-x,D-1-y,z))
                    else:
                        res2[y*wx+(D-1-x)*wy+z*wz] = C
                        used2.add((y,D-1-x,z))
    c1,c2 = color,color
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if (x,y,z) in used1:continue
                if (x,y,z) in block1:
                    if delete(x,y,z,1):
                        block1.remove((x,y,z))
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if (x,y,z) in used2:continue
                if (x,y,z) in block2:
                    if delete(x,y,z,2):
                        block2.remove((x,y,z))
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if (x,y,z) in used1:continue
                if (x,y,z) in block1:
                    res1[x*wx+y*wy+z*wz] = c1
                    c1 += 1
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if (x,y,z) in used2:continue
                if (x,y,z) in block2:
                    res2[x*wx+y*wy+z*wz] = c2
                    c2 += 1
    print(max(c1,c2)-1)
    print(*res1)
    print(*res2)

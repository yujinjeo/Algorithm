import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
s2d2=[list(map(int,input().split())) for _ in range(n)]
ntr=[[5 for _ in range(n)] for _ in range(n)]
tree={}
d=[(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,0),(1,-1),(1,1)]

for i in range(m):
    x,y,z = map(int,input().split())
    if (x-1,y-1) in tree:
        tree[(x-1,y-1)].append(z)
    else:
        tree[(x-1,y-1)]=[z]

def springandsummer():
    global ntr, tree
    for i,j in tree.keys():
        l=len(tree[(i,j)])
        dead=-1
        for t in range(l-1,-1,-1):
            cand = tree[(i,j)][t]
            if ntr[i][j]>=cand:
                ntr[i][j]-=cand
                tree[(i,j)][t]=cand+1
            else:
                dead=t
                break
        if dead==-1:
            tree[(i,j)]=tree[(i,j)][dead+1:]
            continue
        for t in range(dead,-1,-1):
            ntr[i][j]+=tree[(i,j)][t]//2
            
        tree[(i,j)]=tree[(i,j)][dead+1:]
            
def autumn():
    global ntr, tree
    lst=list(tree.keys())
    for i,j in lst:
        cnt=0
        for t in range(len(tree[(i,j)])):
            if tree[(i,j)][t]<5: break
            if tree[(i,j)][t]%5==0:
                cnt+=1
        if not cnt:
            continue
        for dx, dy in d:
            x=i+dx
            y=j+dy
            if 0<=x<n and 0<=y<n:
                # print(x,y)
                if (x,y) in tree:
                    tree[(x,y)].extend([1]*cnt)
                else:
                    tree[(x,y)]=[1]*cnt

def winter():    
    global ntr, tree
    for i in range(n):
        for j in range(n):
            ntr[i][j]+=s2d2[i][j]


for _ in range(k):
    springandsummer()
    autumn()
    winter()
    
ans=0
for i,j in tree.keys():
    ans+=len(tree[(i,j)])

print(ans)

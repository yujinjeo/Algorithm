import sys

input = sys.stdin.readline

dic = {
    1: [[(0,1)],[(1,0)],[(0,-1)],[(-1,0)]],
    2: [[(0,-1),(0,1)],[(1,0),(-1,0)]],
    3: [[(-1,0),(0,1)],[(0,1),(1,0)],[(0,-1),(1,0)],[(0,-1),(-1,0)]],
    4: [[(0,-1),(-1,0),(0,1)], [(-1,0),(0,1),(1,0)],[(0,1),(1,0),(0,-1)],[(1,0),(0,-1),(-1,0)]],
    5: [[(0,1),(0,-1),(-1,0),(1,0)]]  
}

n,m=map(int,input().split())
board=[]

cctv=[]
c=0
for i in range(n):
    lst = list(map(int,input().split()))
    for j in range(m):
        if 0<lst[j]<6:
            cctv.append((lst[j], i,j))
            c+=1

    board.append(lst)

ans=1e9

def check(lst):
    cand=[[False]*(m) for _ in range(n)]
    
    for i in range(c):
        num, x,y=cctv[i]
        turn = lst[i]
        for dx,dy in dic[num][turn]:
            a,b=x+dx,y+dy
            while 0<=a<n and 0<=b<m:
                if board[a][b]==6:
                    break
                cand[a][b]=True
                a+=dx
                b+=dy
    cnt=0
    for i in range(n):
        for j in range(m):
            if not cand[i][j] and not board[i][j]:
                cnt+=1 
 
    return cnt

def bact(lst, idx):
    global ans
    
    if idx==c:
        ans = min(ans,check(lst))
        return

    turn= cctv[idx][0]

    for i in range(len(dic[turn])):
        lst.append(i)
        bact(lst, idx+1)
        lst.pop()
      
bact([], 0)
print(ans)

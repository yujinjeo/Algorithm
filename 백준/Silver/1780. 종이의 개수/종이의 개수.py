import sys

input = sys.stdin.readline

dic={-1:0, 0:0, 1:0}

n=int(input())

board=[list(map(int,input().split(' '))) for _ in range(n)]

def check(x,y,r):
    val=board[x][y]
    for i in range(x,x+r):
        for j in range(y, y+r):
            if board[i][j]!=val:
                nr=r//3
                for a in range(x,x+r,nr):
                    for b in range(y,y+r,nr):
                        check(a,b,nr)
                return
    dic[val]+=1
    return

check(0,0,n)

print(dic[-1])
print(dic[0])
print(dic[1])
            
    

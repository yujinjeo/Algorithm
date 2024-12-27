import sys

input = sys.stdin.readline

n=int(input())

board=[list(map(int,input().split(' '))) for _ in range(n)]

def check(i,j,k):
    cnt=k**2
    s=0
    for a in range(i,i+k):
        for b in range(j,j+k):
            s+=board[a][b]
    if s==0 or s==cnt:
        return (True,board[i][j])
    else:
        return (False,board[i][j])

dic={0:0, 1:0}

def divide(i,j,k):   
    
    is_checked, color = check(i,j,k)
    if is_checked:
        dic[color]+=1
        return 

    m=k//2
    divide(i,j,m)
    divide(i+m,j,m)
    divide(i,j+m,m)
    divide(i+m,j+m,m)

divide(0,0,n)

print(dic[0])
print(dic[1])
    
    


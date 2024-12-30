import sys

input = sys.stdin.readline

n=int(input())
film=[ list(map(str,input().rstrip())) for _ in range(n)]


def is_check(i,j,k):
    s=film[i][j]
    for a in range(i,i+k):
        for b in range(j,j+k):
            if film[a][b]!=s:
                return False
    return True


ans=''
def divide(i,j,k):
    global ans
    if is_check(i,j,k):
        ans+=film[i][j]
        return
    ans+='('
    divide(i,j,k//2)
    divide(i,j+k//2,k//2)
    divide(i+k//2,j,k//2)
    divide(i+k//2, j+k//2, k//2)
    ans+=')'

divide(0,0,n)

print(ans)

import sys
# n 이 100,000 까지 나온다. 
sys.setrecursionlimit(100001)
input = sys.stdin.readline

n=int(input())

inorder= list(map(int,input().split()))
postorder = list(map(int,input().split()))

ans=[]
def func(ix,iy, px, py):
    # print(inorder[ix:iy+1])
    # print(postorder[px:py+1])
    # print("====================")
    global ans
    if ix==iy:
        ans.append(inorder[ix])
        return
    mid = postorder[py]
    ans.append(mid)
    midx=inorder.index(mid)
    if ix<=midx-1 and px<=px+midx-1-ix:
        func(ix,midx-1, px, px+midx-1-ix)
    if midx+1<=iy and px+midx-ix<=py-1:
        func(midx+1, iy, px+midx-ix, py-1)

func(0,n-1, 0, n-1)
print(*ans)
    
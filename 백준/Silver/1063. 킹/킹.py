# #1063 킹 풀기
import sys

def move(xk,yk,xr,yr):
  global board,ki,kj,ri,rj
  if 0 <= xk < 8 and 0 <= yk < 8:
    if xk==ri and yk==rj:
      if 0 <= xr < 8 and 0 <= yr < 8:
        board[ri][rj]=0
        board[xr][yr]=2
        ri=xr
        rj=yr
        board[ki][kj]=0
        board[xk][yk]=1
        ki=xk
        kj=yk
        return
      else:
        return
    else:
      board[ki][kj]=0
      board[xk][yk]=1
      ki=xk
      kj=yk
      return
  else:
    return

    
      

board=[[0]*8 for _ in range(8)]

k,r,n=map(str,sys.stdin.readline().split())

n=int(n)
kj=ord(k[0])-ord('A')
ki=int(k[1])-1
rj=ord(r[0])-ord('A')
ri=int(r[1])-1

#1은 king, 2는 rock
board[ki][kj]=1
board[ri][rj]=2

for i in range(n):
  to=sys.stdin.readline().strip()
  if to=='R':
    move(ki,kj+1,ri,rj+1)
  elif to=='L':
    move(ki,kj-1,ri,rj-1)
  elif to=='B':
    move(ki-1,kj,ri-1,rj)
  elif to=='T':
    move(ki+1,kj,ri+1,rj)
  elif to=='RT':
    move(ki+1,kj+1,ri+1,rj+1)
  elif to=='LT':
    move(ki+1,kj-1,ri+1,rj-1)
  elif to=='RB':
    move(ki-1,kj+1,ri-1,rj+1)
  elif to=='LB':
    move(ki-1,kj-1,ri-1,rj-1)
  else:
    break

print(chr(ord('A')+kj)+str(ki+1))
print(chr(ord('A')+rj)+str(ri+1))

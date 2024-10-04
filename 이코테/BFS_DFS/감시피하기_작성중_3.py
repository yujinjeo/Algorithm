import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n=int(input())
board=[]
students=[]
teachers=[]

for i in range(n):
  lst=list(map(str,input().rstrip().split(' ')))
  for j in range(n):
    if lst[j]=='S':
      students.append((i,j))
    if lst[j]=='T':
      teachers.append((i,j))
  board.append(lst)


def check(lst):
  visited=[[False for _ in range(n)] for _ in range(n)]
  print(lst)



def bact(lst,sx,sy):
  if len(lst)==3:
    check(lst)
    return
  for i in range(sx,n):
    if sy==n-1:
      sy=sy+1
    for j in range(sy,n):
      if (i,j) not in lst and board[i][j]=='X':
        lst.append((i,j))
        bact(lst,i,j)
        lst.remove((i,j))


bact([],0,0)


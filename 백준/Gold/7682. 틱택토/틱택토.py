import sys

input = sys.stdin.readline

def count(lst):
  cntx=lst.count('X')
  cnto=lst.count('O')
  return (cntx, cnto)

def isBingo(board):
  dic={'X':0, 'O':0}

  # 가로 체크 
  for row in board:
    if len(line:=list(set(row))) == 1 and line[0]!='.': dic[line[0]]+=1

  # 세로 체크
  for col in zip(*board):
    if len(line:=list(set(col)))==1 and line[0]!='.' : dic[line[0]]+=1

  # 대각선 체크
  if len(line:=list(set((board[0][0], board[1][1], board[2][2])))) == 1 and line[0]!='.': 
    dic[line[0]]+=1
  if len(line:=list(set((board[2][0], board[1][1], board[0][2])))) == 1 and line[0]!='.':
    dic[line[0]]+=1
    
  return (dic['X'],dic['O'])


def check(lst):
  cntx, cnto = count(lst)

  board=[list(lst[:3]), list(lst[3:6]), list(lst[6:])]
  bx,bo = isBingo(board)

  # 다 찼는데 빙고가 없는 상황
  if bx==0 and bo==0:
    if cntx==5 and cnto ==4:
      return 'valid'
  # x가 이긴 상황
  elif bx<=2 and bo==0:
    if cntx-1==cnto:
      return 'valid'
  elif bo==1 and bx==0:
    if cnto==cntx:
      return 'valid'
    
  return 'invalid'

while (lst:=input().rstrip()) != 'end':
  print(check(lst))
  


import sys

input = sys.stdin.readline

r,c,k= map(int,input().split(' '))

board_=[list(map(int,input().split(' '))) for _ in range(3)]

def check(board):
  h=len(board)
  w=len(board[0])
  if h>r-1 and w>c-1 and board[r-1][c-1]==k:
    return True
  return False

def cal(board, type):
  h=len(board)
  newboard=[]
  w=0

  board=[list(tup) for tup in board]
  
  for i in range(h):
    lst=board[i]
    lst.sort()
    newlst=[]

    # dic=dict()
    # for j in range(len(lst)):
    #   if lst[j]!=0:
    #     if lst[j] not in dic:
    #       dic[lst[j]]=1
    #     else:
    #       dic[lst[j]]+=1
    # for key,value in dic.items():
    #   newlst.append([key,value])

    value=0
    for i in range(len(lst)):
      if lst[i]!=0:
        value=lst[i]
        break
    cnt=0

    
    for j in range(0, len(board[i])):
      if value==lst[j] and lst[j]>0:
        cnt+=1
      elif lst[j]>0:
        newlst.append((value, cnt))
        value=lst[j]
        cnt=1
    if cnt!=0:
      newlst.append((value,cnt))
    else:
      newlst.append((value,1))
      
    newlst.sort(key=lambda x:(x[1],x[0]))
    newlst=[item for tup in newlst for item in tup]
    # newlst=sum(newlst,[])
    w=max(w,len(newlst))
    newboard.append(newlst)

  w=min(100,w)
  for i in newboard:
    i+=[0]*(w-len(i))
    if len(i)>100:
      i=i[:100]
    
  
  # for i in range(h):
  #   tmp=len(newboard[i])
  #   if tmp<w:
  #     for j in range(w-tmp):
  #       newboard[i].append(0)
        
  return newboard if type=="R" else list(zip(*newboard))

time=0

while True:
  if time>100:
    time=-1
    break
  if check(board_):
    break
  if len(board_)>=len(board_[0]):
    board_=cal(board_, "R")
  else:
    board_=cal(list(zip(*board_)),"C")
  time+=1
    

print(time)


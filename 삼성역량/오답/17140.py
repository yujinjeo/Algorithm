import sys

input = sys.stdin.readline

r,c,k= map(int,input().split(' '))

board_=[list(map(int,input().split(' '))) for _ in range(3)]

def check(board):
  h=len(board)
  w=len(board[0])
  # 모든 index에 -1을 처리해야 한다.
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

    # 그리고 나는 sort 한 다음에 수를 셌는데, 여기서는 dict를 사용하고, 마지막에 items() 함수를 사용하여 sort하고 반복문을 쓰지 않고 수를 셌다. 
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
    # 이런 식으로 튜플을 풀 수 있고,
    newlst=[item for tup in newlst for item in tup]
    # 이런 식으로 풀 수도 있다.
    # newlst=sum(newlst,[])
    w=max(w,len(newlst))
    newboard.append(newlst)

  w=min(100,w)
  for i in newboard:
    # append를 쓰지 않아도, [0]*(w-len(i)) 이런 식으로 추가할 수도 있다.
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
    # 그리고 가장 중요한!!! 열과 행을 바꾸는 방법! list(zip(*board)) 
    board_=cal(list(zip(*board_)),"C")
  time+=1
    

print(time)


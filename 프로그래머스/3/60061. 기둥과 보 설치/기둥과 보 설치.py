
def install(board,lst):
    x,y,a=lst[0],lst[1],lst[2]
    if a==0:
        if board[x][y]>0 and y+1<=len(board):
            board[x][y]+=1
            board[x][y+1]+=1
            return True
        else:
            return False
    else:
        if x+1<=len(board) and (board[x][y]>0 or board[x+1][y]>0):
            board[x][y]+=1
            board[x+1][y]+=1
            return True
        else:
            return False
            

def remove(board,lst):
    x,y,a=lst[0],lst[1],lst[2]
    if a==0:
        if board[x][y+1]-1>1:
            board[x][y+1]-=1
            board[x][y]-=1
            return True
        else:
            return False
    else:
        if (board[x-1][y-1]>1 or board[x+2][y-1] >1) :
            board[x][y]-=1
            board[x+1][y]-=1
            return True
        else:
            return False

def possible(answer):
    for x,y,a in answer:
        if a==0:
            if y==0 or [x-1,y,1] in answer or [x,y-1,0] in answer or [x,y,1] in answer:
                continue
            
            return False
        else:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            
            return False
    return True
    

def solution(n, build_frame):
    answer=[]
    
    for lst in build_frame:
        if lst[3]==1:
            answer.append(lst[:3])
            if not possible(answer):
                answer.remove(lst[:3])
        elif lst[:3] in answer:
            answer.remove(lst[:3])  
            if not possible(answer):
                answer.append(lst[:3])
                   
    
    llist=sorted(answer,key=lambda x: (x[0], x[1], x[2]))
    
    return llist
n=int(input())

board=[[' 'for _ in range(n)] for _ in range(n)]

def func(x,y,radius):
    global board
    if radius==1:
        board[x][y]='*'
        return
    newrad=radius//3
    func(x,y,newrad)
    func(x+newrad, y, newrad)
    func(x+newrad*2,y,newrad)
    func(x,y+newrad,newrad)
    func(x,y+newrad*2,newrad)
    func(x+newrad,y+newrad*2,newrad)
    func(x+newrad*2,y+newrad,newrad)
    func(x+newrad*2,y+newrad*2,newrad)

func(0,0,n)

for i in range(n):
    print(''.join(board[i]))

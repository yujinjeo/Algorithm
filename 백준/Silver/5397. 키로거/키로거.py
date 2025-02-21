import sys

input = sys.stdin.readline

def back(ls):
    if ls:
        ls.pop()
    return

def left(ls, rs):
    if ls:
        rs.append(ls.pop())
    return

def right(ls, rs):
    if rs:
        ls.append(rs.pop())
    return

n= int(input())
for _ in range(n):
    ls,rs=[],[]
    lst=list(map(str,input().rstrip()))
    for i in lst:
        if i=='<':
            left(ls,rs)
        elif i=='>':
            right(ls, rs)
        elif i=='-':
            back(ls)
        else:
            ls.append(i)
    while rs:
        ls.append(rs.pop())
    print(''.join(ls))

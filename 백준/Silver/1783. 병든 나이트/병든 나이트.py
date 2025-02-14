import sys

input = sys.stdin.readline

n,m=map(int,input().split(' '))

if n>2:
    if m>6:
        print(m-2)
    elif 4<m<=6:
        print(4)
    else:
        print(m)
elif n==2: print(min(4,1+(m-1)//2))
else:
    print(1)

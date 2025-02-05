import sys

input = sys.stdin.readline

n=int(input())

if n<=2:
    print(1)
else:
    a,b=1,1
    for i in range(3,n+1):
        b,a=a+b,b

    print(b)


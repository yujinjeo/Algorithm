import sys

input = sys.stdin.readline

a,b=map(int,input().split())

def gcb(b,a):
    while b>0:
        a,b=b,a%b
    return a
        
print(''.join('1' for _ in range(gcb(a,b))))
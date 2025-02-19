import sys

input = sys.stdin.readline

# 최대공약수
def gcd(a,b):
    if a>b:
        while b>0:
            a,b=b,a%b
        return a
    else:
        while a>0:
            b,a=a,b%a
        return b

# 최소공배수
def lcd(a,b):
    return (a*b)/gcd(a,b)

x1, y1=map(int,input().split())
x2, y2= map(int,input().split())

# 분모 구하기
y=lcd(y1, y2)

# 분자 구하기
x=x1*(y/y1)+x2*(y/y2)

# 기약분수 만들기
t=gcd(x,y)
print(int(x/t), int(y//t))


import sys

input = sys.stdin.readline

# 유클리드 호제법을 사용하여 x 까지의 소수 리스트를 구한다.
def net(x):
    prime = [True for _ in range(x+1)]
    prime[0], prime[1]=False, False

    for i in range(2, x//2+1):
        for j in range(2,x//i+1):
            prime[i*j]=False
    return prime


lst = []
maxv=0
while True:
    n=int(input())
    if not n :
        break
    maxv=max(maxv, n)
    lst.append(n)
prime=net(maxv*2)
for i in lst:
    print(prime[i+1:i*2+1].count(True))

import sys

input=sys.stdin.readline

n=int(input())

lst=list(map(int,input().split()))
lst.sort()

# 문제에는 '집에' 안테나를 설치한다고 하였다. 그렇다면 당연히 1부터 9까지 찾아볼 필요 없이 너무나 당연히 중앙값이다.
print(lst[(n-1)//2])

import sys

input= sys.stdin.readline

n=int(input())
lst=list(map(int, input().split()))

lst.sort()

# 1부터 시작하면 반드시 1, 2, 3,.. 차례대로 가게 되어 있다. 왜? target이 lst[i]보다 큰 이상, lst[i]이전까지 반드시 연속으로 존재한다. 왜? 1부터 시작해서, lst[i]부터 더함. 그런데 target은 계속 현재 가능한 것에 1을 더한 것임. 그래서 target보다 lst[i]가 작을 경우 반드시 연속되게 되어 있다.
target=1
for i in range(n):
  if target>=lst[i]:
    target+=lst[i]
  else:
    break

print(target)

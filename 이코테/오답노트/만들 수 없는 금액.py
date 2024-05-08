import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

# 1부터 시작한 target을 통해, 1부터 target-1까지는 다 만들 수 있음을 보장하고, 이번에 들어오는 lst[i]를 통해 target을 만들 수 있는지를 확인하는 식으로 진행한다.
# 1부터 시작하는 것이 핵심이다. lst가 오름차순으로 정렬되어 있는 상태에서, 이번 lst[i]가 target보다 작으면, 적어도 lst[i]+1부터 lst[i]+target-1까지는 반드시 만들 수 
# 있기 때문에 lst[i]+target-1까지 연속적으로 금액을 만들 수 있다. 때문에 target을 target+lst[i]로 갱신한다.
# 새로 들어온 값 lst[i]가 target보다 크다면, 지금까지 만들 수 있는 값이 target-1이 최대인데, target-1+lst[i] 부터 만들 수 있는 것이다. 따라서 target이 만들 수 없는 가장
# 작은 값이 되는 것이다.
target=1
lst.sort()
for i in range(n):
  if target<lst[i]:
    break
  else:
    target+=lst[i]

print(target)
    

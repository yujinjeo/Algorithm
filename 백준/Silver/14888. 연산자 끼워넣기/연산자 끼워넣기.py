import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))
# 0 : + , 1 : - , 2 : x , 3 : %
cal=list(map(int,input().split()))

maxval,minval=-10**9,10**9
def dfs(order):
  if cal.count(0)==4:
    count(order)
    return
  for i in range(4):
    if cal[i]!=0:
      order.append(i)
      cal[i]-=1
      dfs(order)
      order.pop()
      cal[i]+=1

def count(order):
  global maxval, minval
  cand=nums[0]
  for i in range(1,n):
    c=order[i-1]
    if c==0:
      cand+=nums[i]
    elif c==1:
      cand-=nums[i]
    elif c==2:
      cand*=nums[i]
    else:
      if cand<0:
        cand=-(abs(cand)//nums[i])
      else:
        cand=cand//nums[i]
  maxval=max(maxval,cand)
  minval=min(minval,cand)

dfs([])
print(maxval)
print(minval)
import sys

input=sys.stdin.readline

n=int(input())
num=list(map(int,input().split(' ')))
opr=list(map(int,input().split(' ')))
# 0 1 2 3
# + - x /
maxval,minval=-10**9,10**9

def calculate(lst):
  val=num[0]
  for i in range(n-1):
    if lst[i]==0:
      val+=num[i+1]
    elif lst[i]==1:
      val-=num[i+1]
    elif lst[i]==2:
      val*=num[i+1]
    else:
      if val<0:
        val=-(abs(val)//num[i+1])
      else:
        val=val//num[i+1]
  return val

def bact(lst):
  global maxval, minval
  if opr.count(0)==4:
    val=calculate(lst)
    maxval=max(maxval,val)
    minval=min(minval,val)
    return
  for i in range(4):
    if opr[i]>0:
      lst.append(i)
      opr[i]-=1
      bact(lst)
      lst.pop(-1)
      opr[i]+=1

bact([])
print(maxval)
print(minval)

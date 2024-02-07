import sys

input=sys.stdin.readline
n=int(input())
lst=list(map(int, input().split()))
pmmd=list(map(int, input().split()))

ans=[]

def bact(picked,cnt,a):
  if cnt==n:
    if a not in ans:
      ans.append(a)
    return
  for i in range(4):
    if pd[i]>0:
      pd[i]-=1
      picked.append(i)
      tmp=a
      if i==0:
        a+=lst[cnt]
      elif i==1:
        a-=lst[cnt]
      elif i==2:
        a*=lst[cnt]
      elif i==3:
        if a<0:
          rr=-a
          rr//=lst[cnt]
          a=-rr
        else:
          a//=lst[cnt]
      bact(picked,cnt+1,a)
      a=tmp
      pd[i]+=1
      picked.pop()

  # if pd[0]>0:
  #   print("+")
  #   pd[0]-=1
  #   a=a+lst[cnt]
  #   bact(cnt+1,a)
  #   pd[0]+=1
  #   a-=lst[cnt]
  # if pd[1]>0:
  #   print("-")
  #   pd[1]-=1
  #   a=a-lst[cnt]
  #   bact(cnt+1,a)
  #   pd[1]+=1
  #   a+=lst[cnt]
  # if pd[2]>0:
  #   print("*")
  #   pd[2]-=1
  #   tmp=a
  #   a*=lst[cnt]
  #   bact(cnt+1,a)
  #   pd[2]+=1
  #   a=tmp
  # if pd[3]>0:
  #   print("/")
  #   pd[3]-=1
  #   tmp=a
  #   a//=lst[cnt]
  #   bact(cnt+1,a)
  #   pd[3]+=1
  #   a=tmp
  
pd=pmmd.copy()
picked=[]
bact(picked,1,lst[0])

ans=sorted(ans)
print(ans[-1])
print(ans[0])
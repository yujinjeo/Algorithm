import sys
input=sys.stdin.readline

#sol 1
tmp=input().strip()
lst=list(map(int,tmp))

lst.sort(reverse=True)
answer=lst[0]
for i in range(1,len(lst)):
  if lst[i]!=0:
    answer*=lst[i]
  else:
    answer+=lst[i]

print(answer)


#sol 2 - 'velmash' 님의 블로그에 나온 풀이
lst=input().strip()
answer=int(lst[0])
for i in range(1,len(lst)):
  if int(lst[i])<=1 or answer<=1:
    answer+=int(lst[i])
  else:
    answer*=int(lst[i])

print(answer)

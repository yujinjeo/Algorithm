import sys

input=sys.stdin.readline

n=int(input())
dic={}
for i in range(n):
  k,v=map(str,input().strip().split(' '))
  dic[k]=int(v)

# lambda 함수 사용하는 방법 1
# lambda 변수 : 출력값
# sorted(정렬할 리스트, key = lambda ... : ...)

# 딕셔너리의 items()는 key와 value로 이루어진 ###튜플### 들의 리스트입니다.
lst=list(sorted(dic.items(), key=(lambda item : item[1])))

for i in range(n):
  print(lst[i][0],end=' ')

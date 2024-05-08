##오답노트는 제한시간에 문제를 풀지 못해 답지를 보고 푼 풀이를 말합니다!
import sys
input=sys.stdin.readline

str=input().strip()
cnt1=0
cnt0=0
c=str[0]
for i in range(1,len(str)):
  if c!=str[i]:
    if c=='0':
      cnt0+=1
      c='1'
    else:
      cnt1+=1
      c='0'

print(min(cnt0,cnt1))

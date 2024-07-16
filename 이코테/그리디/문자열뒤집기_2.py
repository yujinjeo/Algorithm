str=input().rstrip()

answer=0
# 전부 1로 만들어야 할 때의 cnt1, 전부 0으로 만들어야 할 때의 cnt0
cnt0, cnt1=0,0

# 왜 첫 번째 요소에 대한 확인 과정이 필요한가?
# 가장 먼저 변한 것에 대한 cnt만 세고, 그 반대의 것은 하나 세지 않기 때문이다. 
# 예를 들어, 01... 이러한 것이 있을 때, cnt0 만 세고, 첫 번째 원소에 대한 cnt1은 1개가 빠지기 때문이다. 
if str[0]=='0':
  cnt1+=1
else:
  cnt0+=1


for i in range(len(str)-1):
  if str[i]!=str[i+1]:
    if str[i+1]=='0':
      cnt1+=1
    else:
      cnt0+=1

print(min(cnt0,cnt1))
      
  


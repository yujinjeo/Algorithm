import sys

l=sys.stdin.readline().strip()
n=len(l)
answer=''
sum=0
for i in range(n):
  if '0'<=l[i]<='9':
    sum+=int(l[i])
  else:
    answer+=l[i]

#print(sorted(answer)) # 결과 : 정렬된 문자 배열 !!!  따라서 join 함수가 필요하다.

answer=''.join(sorted(answer))+str(sum)
print(answer)

import sys

n=int(sys.stdin.readline())
ans=[]
for _ in range(n):
  ans.append(sys.stdin.readline().strip())

#sorted 함수의 key 속성과 lambda 함수를 사용한 정렬
ans=sorted(ans, key=lambda x:(len(x),x))

#dict을 사용한 중복제거
#fromkeys 함수를 사용하면 리스트들을 딕셔너리로 바꿀 수 있는데 바꾸는 과정에서 자동으로 key들에 대한 중복에 제거된다.
ans=list(dict.fromkeys(ans))

for a in ans:
  print(a)
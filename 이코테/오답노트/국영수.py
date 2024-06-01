import sys

input=sys.stdin.readline
n=int(input())

dic={}

for i in range(n):
  s,k,e,m=map(str,input().strip().split(' '))
  lst=[int(k),int(e),int(m)]
  dic[s]=lst

# sorted 의 key 정렬 변수를 여러 개 지정하고 싶다면 return 부분에 () 소괄호 안에 변수를 넣는다.
# 중간에 reverse 처리하고 싶은 게 있다면, 변수의 값에 음수처리 해주면 된다! 

# sort함수와 달리 sorted 함수는 list를 직접 바꾸지는 않는다. 따라서 items 라는 리턴값으로 반드시 받아야 한다. 
items=sorted(dic.items(), key=lambda item: (-item[1][0], item[1][1], -item[1][2], item[0]))

for i in range(n):
  print(items[i][0])

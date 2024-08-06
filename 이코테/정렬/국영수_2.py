import sys

input=sys.stdin.readline

n=int(input())

lst=[]
for _ in range(n):
  name,a,b,c=map(str,input().rstrip().split(' '))
  lst.append((name,int(a),int(b),int(c)))

lst.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in range(n):
  print(lst[i][0])

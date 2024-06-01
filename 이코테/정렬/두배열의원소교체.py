import sys
input=sys.stdin.readline

n,k=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort(reverse=True)
da=0
db=0

for i in range(k):
  if a[da]<b[db]:
    tmp=a[da]
    a[da]=b[db]
    b[db]=tmp
    da+=1
    db+=1

print(sum(a))


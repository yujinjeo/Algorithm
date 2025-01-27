from collections import deque
import sys

input = sys.stdin.readline
lst=[]

s=input().rstrip()
num=''
pre=''
for i in range(len(s)):
    if s[i] not in ['+','-']:
        num+=s[i]
    else:
        if pre=='+':
            a=lst.pop()
            lst.append(a+int(num))   
        else:
            lst.append(int(num))
        pre=s[i]
        num=''
if pre=='+':
    a=lst.pop()
    lst.append(a+int(num))   
else:
    lst.append(int(num))

q=deque(lst)
a=q.popleft()
while q:
    a-=q.popleft()

print(a)
        

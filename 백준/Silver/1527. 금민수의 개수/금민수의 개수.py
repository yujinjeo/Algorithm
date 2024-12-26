
# 브루트 포스? -> 시간 초과
from itertools import product
a,b=map(int,input().split(' '))
ans=0

# 1의 자리부터 9의 자리까지 자리 단위를 늘려가면서 
low=len(str(a))
high=len(str(b))
flag=0
for i in range(low,high+1):
    lst = product(['4','7'],repeat = i)
    for c in lst:
        cand=int(''.join(c))
        if a<=cand<=b:
            ans+=1
        elif cand>b:
            flag=1
            break
    if flag:
        break

print(ans)


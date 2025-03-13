import sys

input = sys.stdin.readline
t=int(input())

def func(i):
    x = lst[i]
    l=1
    cnt=1
    for j in range(i+1, len(lst)):
        if cnt==n:
            return l
        l+=1
        if lst[j]==x:
            cnt+=1
    return -1

for _ in range(t):
    lst= list(map(str, input().rstrip()))
    n=int(input())
    if n==1:
        print(1, 1)
        continue

    minans=1e9
    maxans=0
    dic={}
    for i in range(len(lst)):
        c = lst[i]
        if c not in dic:
            dic[c]=[i]
        else:
            dic[c].append(i)

    for key in dic.keys():
        if len(dic[key])<n:
            continue
        for i in range(len(dic[key])-(n-1)):
            cand=dic[key][i+n-1]-dic[key][i]+1
            minans=min(minans, cand)
            maxans=max(maxans, cand)
    if not maxans:
        print(-1)
    else:
        print(minans, maxans)
        

    
    # for i in range(len(lst)):
    #     cand = func(i)
    #     if cand == -1:
    #         continue
    #     minans=min(minans, cand)
    #     maxans=max(maxans, cand)
    # if minans==1e9:
    #     print(-1)
    # else:
    #     print(minans, maxans)
    
    
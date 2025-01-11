n,m=map(int,input().split(' '))

lst=list(map(int,input().split(' ')))

def check(x):
    sum=0
    cnt=0
    for i in range(n):
        if lst[i]>x:
           return False
        if sum+lst[i]<=x:
            sum+=lst[i]
        else:
            sum=lst[i]
            cnt+=1
    if cnt<m:
        return True
    else:
        return False
            
    
ans=0

def bin(s,e):
    global ans
    if s>e:
        return
    m=(s+e)//2
    if check(m):
        ans=m
        bin(s,m-1)
    else:
        bin(m+1,e)

bin(1,sum(lst))
print(ans)
        

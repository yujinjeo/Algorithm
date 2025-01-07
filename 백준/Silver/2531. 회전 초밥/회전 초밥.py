n,d,k,c=map(int,input().split(' '))

lst=[int(input()) for _ in range(n)]

val=1
visited=[0]*(d+1)
visited[c]=1

for j in range(k):
    visited[lst[j%n]]+=1
    if visited[lst[j%n]]==1:
        val+=1

cand=val

for i in range(1,n):
    visited[lst[i-1]]-=1
    if visited[lst[i-1]]==0:
        cand-=1

    visited[lst[(i+k-1)%n]]+=1
    if visited[lst[(i+k-1)%n]]==1:
        cand+=1
    
    val=max(val, cand)
    

print(val)
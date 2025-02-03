import sys

input = sys.stdin.readline

n=int(input())
cranes=list(map(int,input().split(' ')))
cranes.sort(reverse=True)

m=int(input())
boxes=list(map(int,input().split(' ')))
boxes.sort(reverse=True)

ans=0
if cranes[0]<boxes[0]: ans=-1
else:
    while boxes:
        i=0
        j=0
        while i<n and j<len(boxes):
            if cranes[i]>=boxes[j]:
                boxes.pop(j)
                i+=1
            else:
                j+=1
        ans+=1
    
print(ans)


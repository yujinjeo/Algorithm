import sys

input = sys.stdin.readline

n=int(input())
switch=[-1]+list(map(int,input().split(' ')))

m=int(input())

def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

def women(x):
    switch[x]=(switch[x]+1)%2
    for i in range(1,n//2+1):
        r=x+i
        l=x-i
        if 1<=l and r<=n:
            if switch[l]==switch[r]:
                change(l)
                change(r)
            else:
                break
        else:
            break
    
def men(x):
    for i in range(x, n+1, x):
            change(i)

for _ in range(m):
    sex, num= map(int,input().split(' '))
    if sex-1:
        women(num)
    else:
        men(num)

for i in range(1,n+1):
    if i%20==0:
        print(switch[i])
    else:
        print(switch[i],end=' ')
        

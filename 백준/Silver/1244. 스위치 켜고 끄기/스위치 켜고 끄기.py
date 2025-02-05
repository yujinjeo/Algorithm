import sys

input = sys.stdin.readline

n=int(input())
switch=[-1]+list(map(int,input().split(' ')))

m=int(input())

def women(x):
    switch[x]=(switch[x]+1)%2
    for i in range(1,n//2+1):
        r=x+i
        l=x-i
        if 1<=l and r<=n:
            if switch[l]==switch[r]:
                switch[l]=switch[r]=(switch[l]+1)%2
            else:
                break
    
def men(x):
    for i in range(x, n+1, x):
        switch[i]=(switch[i]+1)%2

for _ in range(m):
    sex, num= map(int,input().split(' '))
    if sex-1:
        women(num)
    else:
        men(num)

for i in range(1,n+1):
    print(switch[i],end=' ')
    if i%20==0:
        print()
        

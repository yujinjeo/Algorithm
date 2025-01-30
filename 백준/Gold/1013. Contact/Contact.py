import sys

input = sys.stdin.readline

t=int(input())

for _ in range(t):
    l=input().rstrip()
    n=len(l)
    if n==1:
        print('NO')
        break

    # 1 . '01' 부분 2로 만들기
    l='1'+l
    pre='1'
    idx=1
    
    new=''
    while idx-1<n:
        if pre=='1':
            if l[idx:idx+2]=='01':
                new+='2'
                idx+=2
                continue
        new+=l[idx]
        pre=l[idx]
        idx+=1
    new+=l[idx:]
    
    # 2 . '100+1' 부분 3으로 만들기
    tmp=new[0]
    new2=''
    idx=1
    for i in range(1,len(new)):
        if new[i]=='0':
            tmp+=new[i]
        elif new[i]=='1':
            if len(tmp)>=3 and tmp[:3]=='100':
                tmp+=new[i]
                new2+='3'
                tmp=''
            else:
                new2+=tmp
                tmp='1'
        else:
            new2+=tmp
            tmp=new[i]
    new2+=tmp

    # 3. check
    fail=False
    isok=False
    for i in range(1,len(new2)):
        if new2[i]=='1':
            if new2[i-1]=='3':
                isok=True
            elif new2[i-1]=='1' and isok:
                continue
            else:
                fail=True
                break
        if new2[i]=='0':
            fail=True

    if new2[0]=='1':
        fail=True
        
    if fail:
        print('NO')
    else:
        print('YES')

    
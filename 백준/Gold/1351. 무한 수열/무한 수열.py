n,p,q=map(int,input().split(' '))

dic={0:1, 1:2}

def func(x):
    if x in dic:
        return dic[x]
    # 코끼리 연산자는 변수를 새로 만드는 데에는 사용할 수 없음
    # return dic[x]:=func(x//p)+func(x//q)
    dic[x]=func(x//p)+func(x//q)
    return dic[x]

print(func(n))

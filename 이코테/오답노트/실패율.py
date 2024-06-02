idx=0

def failrate(stages, k):
    global idx
    n=len(stages)
    total=n-idx
    r=idx
    for i in range(r,n):
        if stages[i]>k:
            break
        idx+=1
    cnt=idx-r
   ## 문제에서 0 이라고 정의해줬기 때문에 이렇게 작성해줘야 한다!
    if cnt==0:
        answer=0
    else:
        answer=cnt/total
    
    print(answer)
    
    return answer



def solution(N, stages):
    global idx
    answer=[]
    stages.sort()
    
    fails={}
    idx=0
    # 각 스테이지별 실패율
    for i in range(1,N+1):
        fails[i]=failrate(stages,i)
        
    lst=sorted(fails.items(), key= lambda item:item[1], reverse=True)
    for item in lst:
        answer.append(item[0])
    
    return answer

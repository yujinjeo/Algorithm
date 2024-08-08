def solution(N, stages):
    answer = []
    fail_rate=[]
    stages.sort()
    m=len(stages)
    
    for i in range(1,N+1):
        
        cnt=stages.count(i)
        
        if cnt>0:
            idx=stages.index(i)
            fail_rate.append((i,cnt/(m-idx)))
        else:
            fail_rate.append((i,0))
    
    fail_rate.sort(key=lambda x:-x[1])
    for i in range(N):
        answer.append(fail_rate[i][0])
        
    return answer

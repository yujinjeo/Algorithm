from itertools import permutations

def solution(n, weak, dist):
    d = len(dist)
    m = len(weak)
    
    answer=d+1
    
    for i in range(len(weak)):
        weak.append(weak[i]+n)
    
    for start in range(m):
        cand=d+1
        
        for lst in list(permutations(dist, d)):
            idx=0
            cnt=1
            present=weak[start]+lst[idx]
            for i in range(start,start+m):
                if present < weak[i]:
                    cnt+=1
                    if cnt>d:
                        break
                    idx+=1
                    present=weak[i]+lst[idx]
                    
                    
            cand=min(cand, cnt)
        answer=min(answer,cand)
        
    if answer > d:
        answer=-1
    
    
    return answer
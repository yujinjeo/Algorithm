import itertools

def solution(k, dungeons):
    answer = -1
    n=len(dungeons) 
    
    orders=itertools.permutations(dungeons, n)
    for order in orders:
        k_v=k
        cnt=0
        for a,b in order:
            if k_v>=a:
                k_v-=b
                cnt+=1
        
        answer=max(answer,cnt)
    
    return answer
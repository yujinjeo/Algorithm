from collections import Counter

def solution(clothes):
    answer = 1
    ll=[]
    for i in range(len(clothes)):
        ll.append(clothes[i][1])
        
    dic=Counter(ll)
    val=list(dic.values())
    
    for i in range(len(val)):
        answer*=(val[i]+1)
        
    answer-=1
    
    
    return answer
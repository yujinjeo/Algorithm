def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n-1):
        cnt = 1
        for j in range(i+1,n-1):
            if prices[i] > prices[j]:
                break
            cnt += 1
        answer.append(cnt)
    answer.append(0)
    
    
                
    return answer
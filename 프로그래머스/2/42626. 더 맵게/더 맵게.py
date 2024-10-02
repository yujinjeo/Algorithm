import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>1:
        test=heapq.heappop(scoville)
        if k<=test:
            break
        heapq.heappush(scoville,test)
        
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer+=1

    if len(scoville)==1 and scoville[0]<k:
        answer=-1
    
    
    
    return answer
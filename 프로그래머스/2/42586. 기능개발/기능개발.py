from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    sq=deque(speeds)
    
    while queue:
        n=len(queue)
        cnt=0
        for i in range(n):
            queue[i] += sq[i]
        cand=queue.popleft()
        if cand >= 100:
            cnt+=1
            sq.popleft()
            k=len(queue)
            for i in range(k):
                child=queue.popleft()
                if child>=100:
                    sq.popleft()
                    cnt+=1
                else:
                    queue.appendleft(child)
                    break
        else:
            queue.appendleft(cand)
        if cnt>0:
            answer.append(cnt) 
        print(queue)
     
    return answer
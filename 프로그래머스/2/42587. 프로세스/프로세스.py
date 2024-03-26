from collections import deque

def solution(priorities, location):
    answer = 1
    queue=deque(priorities)
    tmp = [0 for _ in range(len(priorities))]
    tmp[location]=1
    processes = deque(tmp)
    
    while queue:
        priority = queue.popleft()
        process = processes.popleft()
        if any(priority < current_process for current_process in queue):
            queue.append(priority)
            processes.append(process)
        elif process == 1:
            break
        else:
            answer+=1
    return answer 
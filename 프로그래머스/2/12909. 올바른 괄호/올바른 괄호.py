from collections import deque

def solution(s):
    answer = True
    q=deque()
    for i in range(len(s)):
        if s[i]=='(':
            q.append(s[i])
        else:
            if len(q)>0:
                q.pop()
            else:
                answer=False
                break
    if len(q)!=0:
        answer=False
    return answer
def impossible(answer):
    for [x,y,a] in answer:
        if a==0:
            if y!=0 and [x,y-1,0] not in answer and \
            [x-1,y,1] not in answer and [x,y,1] not in answer:
                return True
        else:
             if [x,y-1,0] not in answer and [x+1,y-1,0] not in answer and \
                ([x-1,y,1] not in answer or [x+1,y,1] not in answer):
                    return True
    return False

def solution(n, build_frame):
    answer = []
    for x,y,a,build in build_frame:
        if build:
            answer.append([x,y,a])
            if impossible(answer):
                answer.remove([x,y,a])
        elif [x,y,a] in answer:
            answer.remove([x,y,a])
            if impossible(answer):
                answer.append([x,y,a])
    
    answer.sort(key=lambda x : (x[0],x[1],x[2]))
    return answer

def solution(s):
    answer = 0
    stack=[s[0]]
    for i in range(1,len(s)):
        if len(stack)==0 or stack[0]==s[i]:
            stack.append(s[i])
        else:
            stack.pop(-1)
        if len(stack)==0:
            answer+=1
    if len(stack)!=0:
        answer+=1
    return answer
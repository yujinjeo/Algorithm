def solution(number, k):
    lst=list(map(str,number))
    
    n=len(lst)
    stack =[]
    for i in range(n):
        num=lst[i]
        if not stack or not k:
            stack.append(num)
        else:
            while stack[-1]<num:
                stack.pop()
                k-=1
                if not stack or k<=0:
                    break
                
            stack.append(num)
    
    answer = ''.join(stack[:len(stack)-k])
    return answer
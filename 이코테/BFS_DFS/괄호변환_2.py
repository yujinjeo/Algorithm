def to_balanced(w):
    n=len(w)
    idx=0
    u,v='',''
    cntl=0
    cntr=0
    for i in range(n):
        if w[i]=='(':
            cntl+=1
        else:
            cntr+=1
            
        if cntl==cntr:
            idx=i
            break
    return (w[:i+1],w[i+1:])

def is_correct(u):
    if u=='':
        return True
    cnt=0
    if u[0]=='(':
        cnt+=1
    else:
        return False
    for i in range(1,len(u)):
        if u[i]=='(':
            cnt+=1
        else:
            cnt-=1
    if cnt==0:
        return True
    else:
        return False

def change_u(u):
    res=''
    for a in u:
        if a=='(':
            res+=')'
        else:
            res+='('
    return res

def solution(p):
    answer = ''
    
    if p=='':
        return p
    u,v=to_balanced(p)
    if is_correct(u):
        corrected_v=solution(v)
        answer=u+corrected_v
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'
        l=len(u)
        u=u[1:l-1]
        u=change_u(u)
        answer+=u

    return answer

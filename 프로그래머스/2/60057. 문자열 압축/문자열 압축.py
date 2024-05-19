def count_s(s,n):
    string = ''
    word=s[:n]
    cnt=1
    for i in range(n,len(s),n):
        if s[i:i+n]==word:
            cnt+=1
        else:
            if cnt>1:
                string+=str(cnt)
            string+=word
            word=s[i:i+n]
            cnt=1
    if cnt>1:
        string+=str(cnt)
    string+=word
    return len(string)        

def solution(s):
    answer = len(s)
    for i in range(1,len(s)+1):
        c=count_s(s,i)
        answer=min(answer,c)
    
    return answer
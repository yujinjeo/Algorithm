def solution(s):
    answer = 0
    str_lst=[]
    for unit in range(1, len(s)+1):
        cnt=1
        string=""
        for a in range(0, len(s), unit):
            if s[a:a+unit]==s[a+unit:a+2*unit]:
                cnt+=1
            elif cnt>1:
                string+=str(cnt)+s[a:a+unit]
                cnt=1
            else:
                string+=s[a:a+unit]
        str_lst.append(string)

    answer=min(len(ss) for ss in str_lst)
    # val=len(str_lst[0])
    # for i in range(1,len(str_lst)):
    #     val=min(val,len(str_lst[i]))
    # answer=val
    return answer
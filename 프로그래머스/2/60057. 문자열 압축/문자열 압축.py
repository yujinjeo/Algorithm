def solution(s):
    answer = 0
    cut=1
    lengths=[]
    while cut<len(s):
        cand=''
        
        term=s[0:cut]
        cnt=1
        start=cut
        while start<len(s):
            if term==s[start:start+cut]:
                cnt+=1
            else:
                if cnt>1:
                    cand+=str(cnt)
                cand+=term
                term=s[start:start+cut]
                cnt=1
                
            start+=cut
        if term==s[start:]:
            cnt+=1
            if cnt>1:
                cand+=str(cnt)
            cand+=term
        else:
            if cnt>1:
                cand+=str(cnt)
            cand+=term
            cand+=s[start:]
        lengths.append(len(cand))
        cut+=1
    lengths.append(len(s))   
    
    return min(lengths)
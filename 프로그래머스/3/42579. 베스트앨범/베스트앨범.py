def solution(genres, plays):
    from collections import Counter
    
    answer = []
    mydict={}
    mydict2={}
    ger=list(Counter(genres))
    
    #장르별 총 재생 횟수
    for i in range(len(genres)):
        if genres[i] in mydict:
            mydict[genres[i]]+=plays[i]
            mydict2[genres[i]].append(i)
        else:
            mydict[genres[i]]=plays[i]
            mydict2[genres[i]]=[i]
    
    #장르별 총 재생 횟수는 곧 무슨 장르인지를 알 수 있는 지표가 된다.
    a=list(mydict.values())
    a.sort(reverse=True)
    b=[]
    for i in a:
        for j in ger:
            if i==mydict[j]:
                b.append(j)
    
    
    #각 장르별로 plays에 대한 정렬을 해야한다. 
    for i in b:
        if len(mydict2[i])==1:
            answer.append(mydict2[i][0])
        else:
            m=0
            n=0
            for j in mydict2[i]:
                if m<plays[j]:
                    m=plays[j]
                    n=j
            answer.append(n)
            mydict2[i].remove(n)
            m=0
            n=0
            for j in mydict2[i]:
                if m<plays[j]:
                    m=plays[j]
                    n=j
            answer.append(n)
            
    return answer
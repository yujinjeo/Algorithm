def solution(citations):
    answer = 0
    citations=sorted(citations,reverse=True)
    for index, cit in enumerate(citations):
        can=min(index+1, cit)
        answer=max(answer,can)
    return answer
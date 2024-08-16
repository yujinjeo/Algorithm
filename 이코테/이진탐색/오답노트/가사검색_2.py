from bisect import bisect_left, bisect_right

def cnt(lst, query):
    lst.sort()
    # 문자열.replace([old 문자열],[바꾸고자 하는 new 문자열]) 을 사용하여 쉽게 변환할 수 있다.
    s=bisect_left(lst,query.replace('?','a'))
    e=bisect_right(lst,query.replace('?','z'))
    return e-s
        

def solution(words, queries):
    answer = []
    # words를 단어 길이에 따라 나누기
    l=[[] for _ in range(10001)]
    lr=[[] for _ in range(10001)]
    for word in words:
        l[len(word)].append(word)
        # 파이썬에서 문자열을 뒤집을 수 있는 방법은 [::-1] 이다!!
        lr[len(word)].append(word[::-1])
        
    
    for query in queries:
        if query[-1]!='?':
            c=cnt(lr[len(query)],query[::-1])
            answer.append(c)
        else:
            c=cnt(l[len(query)], query)
            answer.append(c)

    
    return answer

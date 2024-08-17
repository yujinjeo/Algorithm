
# sol1 : 이진탐색을 통해 푸는 법

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


# sol2 : trie 구조를 사용하여 푸는 방법

def add(head,word):
    node=head
    for w in word:
        # 상위 노드에 key 추가
        if w not in node:
            node[w]={}
        # 본 노드에 len 추가
        node=node[w]
        if 'len' not in node:
            node['len']=[len(word)]
        else:
            node['len'].append(len(word))
    node['end']=True
    
def search(head, query):
    node=head
    for q in query:
        if q=='?':
            return node['len'].count(len(query))
        if q not in node:
            break
        node=node[q]
    return 0
    


def solution(words, queries):
    lst={}
    rlst={}
    allcnt=[]
    
    for word in words:
        add(lst,word)
        add(rlst,word[::-1])
        allcnt.append(len(word))
    
    answer = []
    for query in queries:
        if query[-1]=='?':
            if query[0]=='?':
                answer.append(allcnt.count(len(query)))
            else:
                answer.append(search(lst,query))
        else:
            answer.append(search(rlst,query[::-1]))        
    
    return answer

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
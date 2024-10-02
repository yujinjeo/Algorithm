import itertools

def is_primary(number):
    if number<2:
        return False
    
    for i in range(2,int(number/2)+1):
        if number%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    nlist=set()
    lst=list(map(str,numbers))
    
    for i in range(1,len(numbers)+1):
        target_lst= itertools.permutations(lst,i)
        for t in target_lst:
            target=int(''.join(t))
            if is_primary(target):
                nlist.add(target)
                
    
    answer=len(nlist)
    
    return answer
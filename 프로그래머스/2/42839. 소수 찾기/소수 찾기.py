import math
from itertools import permutations

def check(x):
    if x<2:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True


def solution(numbers):
    answer = set()
    lst = list(map(str, numbers.rstrip()))
    n=len(lst)
    
    for i in range(1,n+1):
        for l in permutations(lst,i):
            cand=int(''.join(l))
            if cand in answer:
                continue
            if check(cand):
                answer.add(cand)

    return len(answer)
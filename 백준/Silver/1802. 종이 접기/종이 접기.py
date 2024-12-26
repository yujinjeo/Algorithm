# https://velog.io/@rkdwldnjs30/%EB%B0%B1%EC%A4%80python-1802-%EC%A2%85%EC%9D%B4%EC%A0%91%EA%B8%B0
import sys

input = sys.stdin.readline

total=int(input())

def divide(part):
    n=len(part)
    middle=n//2
    if n==1:
        return True
    left_part=part[0:middle]
    right_part=part[middle+1:n]

    
    is_left=divide(left_part)
    is_right=divide(right_part)
    if not is_left or not is_right:
        return False
    
    for i in range(middle):
        if left_part[i]==right_part[middle-1-i]:
            return False
    return True
    

for i in range(total):
    lst=list(map(str,input().rstrip()))
    is_result = divide(lst)
    if is_result:
        print('YES')
    else:
        print('NO')


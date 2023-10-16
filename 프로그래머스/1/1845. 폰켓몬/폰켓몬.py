def solution(nums):
    #변수 지정
    answer = 0
    N=len(nums)
    k=len(set(nums))
    
    if k<N/2:
        #뽑을 수 있는 경우의 수가 얼마 없는 경우
        return k
    return N/2
    
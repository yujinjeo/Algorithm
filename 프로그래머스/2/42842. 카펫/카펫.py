def solution(brown, yellow):
    answer = []
    
    n=int((brown-4)/2)
    y=1
    x=n-y
    
    for i in range(2,n+1):
        if x*y==yellow:
            break
        y=i
        x=n-y
        
    
    answer=[x+2,y+2]
    return answer
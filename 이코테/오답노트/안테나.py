import sys, math

input = sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
# 최대값을 float('inf') 와 같이 설정할 수 있다.
# map 함수의 첫 번째 인수는 함수, 두 번째 인수는 반복 가능한 자료이어야 합니다. 

# 중간값을 선택하면 된다.
### 중간값 (median) 은 리스트의 각 요소와의 절대 차이의 값을 최소화하는 값이다. 이는 중간값의 중요한 성질 중 하나로,
### 통계에서 애우 유용하게 사용됩니다. 모든 요소들과 중간값의 차이의 합을 S라고 할 때,
### 다른 요소를 선택할 경우 S가 최소화되지 않음을 수학적으로 증명할 수도 있다.
lst.sort()
print(lst[(n-1)//2])

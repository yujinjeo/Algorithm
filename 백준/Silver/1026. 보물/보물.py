import sys

n=int(sys.stdin.readline())

A=list(map(int, sys.stdin.readline().split()))
B=list(map(int, sys.stdin.readline().split()))
    
A.sort()
B.sort(reverse=True)

sum_T=sum(map(lambda i:A[i]*B[i],range(len(A))))

print(sum_T)
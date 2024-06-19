import sys

input = sys.stdin.readline
n=int(input())
lst = list(map(int, input().split(' ')))

answer =-1
start = 0
end = n-1

while start <= end:
  middle = (start+end)//2
  if lst[middle]==middle:
    answer=middle
    break
  if lst[middle]>middle:
    end=middle-1
  else:
    start = middle+1

print(answer)

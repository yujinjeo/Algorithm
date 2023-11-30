import sys

n=int(sys.stdin.readline())

endNum=666
t=0
while True:
  if '666' in str(endNum):
    t+=1
  if t==n:
    break 
  endNum+=1

print(endNum)
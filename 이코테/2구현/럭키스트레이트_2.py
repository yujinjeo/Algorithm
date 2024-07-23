import sys
input = sys.stdin.readline

string = input().rstrip()

n=len(string)
middle=n//2
lefts=0
rights=0
for i in range(middle):
  lefts+=int(string[i])
  rights+=int(string[middle+i])

if lefts==rights:
  print('LUCKY')
else:
  print('READY')

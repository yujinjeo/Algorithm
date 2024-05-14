import sys
str=sys.stdin.readline().strip()
lst=[int(i) for i in str]
n=len(str)

if sum(lst[:(n//2)])==sum(lst[(n//2):]):
  print("LUCKY")
else:
  print("READY")

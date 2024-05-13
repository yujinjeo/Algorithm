import sys
input=sys.stdin.readline

n=int(input())

# 1_ 2_분 3_ 4_ 초
# 1 : 0, 1, 2, 4, 5 => 5
# 2 : 0,1,2,4,5,6,7,8,9 => 9 
# 시간 : 3, 13, 23 
answer=(5*9)*(5*9)

if n<3:
  answer*=(n+1)
elif n<13:
  answer*=(n+1-1)
elif n<23:
  answer*=(n+1-2)
else:
  answer*=(n+1-3)

print((n+1)*60*60-answer)

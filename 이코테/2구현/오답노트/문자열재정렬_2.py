import sys
input = sys.stdin.readline

string=[]
ints=0

inputo=input().rstrip()

for a in inputo:
  if a.isalpha():
  # if 'A'<=a<='Z':
    string.append(a)
  else:
    ints+=int(a)

string.sort()
# str(ints)

# answer=''
# for a in string:
#   answer+=a

# print(answer+str(ints))

if ints!=0:
  string.append(str(ints))

#join 사용 - 구분자.join(반복리스트)
print(''.join(string))

import sys

input = sys.stdin.readline

stack=list(map(str,input().rstrip()))
m=int(input())

buffer=[]

def left():
    if stack:
        buffer.append(stack.pop())

def right():
    if buffer:
        stack.append(buffer.pop())

def delete():
    if stack:
        stack.pop()

def plus(x):
    stack.append(x)

for _ in range(m):
    command=list(map(str,input().rstrip().split(' ')))
    if command[0]=='L':
        left()
    elif command[0]=='D':
        right()
    elif command[0]=='B':
        delete()
    else:
        plus(command[1])

stack.extend(reversed(buffer))
print(''.join(stack))




import sys

#max heap 추가 함수
def heappush(heap,data):
  #append하면 맨 뒤에 있으므로 올라가야 한다.
  heap.append(data)
  size=len(heap)
  idx=size-1

  while idx>0:
    parent=(idx-1)//2
    if heap[parent]<heap[idx]:
      tmp=heap[parent]
      heap[parent]=heap[idx]
      heap[idx]=tmp
    else:
      break
    idx=parent  
  
#max heap 삭제 함수
def heappop(heap):
  if len(heap)==0:
    return 0

  value=heap[0]
  
  #자식이 없거나 한쪽만 있을 때
  if len(heap)>1:
    heap[0]=heap.pop()
    size=len(heap)
    parent=0
    
    while parent<size:
      idx=parent
      childleft=2*parent+1
      childright=2*parent+2
      if childleft<size and heap[idx]<heap[childleft]:
        idx=childleft
      if childright<size and heap[idx]<heap[childright]:
        idx=childright

      if idx!=parent:
        tmp=heap[idx]
        heap[idx]=heap[parent]
        heap[parent]=tmp
        parent=idx
        continue
      else:
        break
  else:
    heap.pop()
  return value

#필요한 필드 준비
n=int(sys.stdin.readline())
inputs=[int(sys.stdin.readline()) for _ in range(n)]
heap=[]
ans=[]

#입력에 따른 함수처리, 결과값 추출
for k in inputs:
  if k==0:
    ans.append(heappop(heap))
    continue
  else:
    heappush(heap,k)
    continue

#결과 출력
for a in ans:
  print(a)

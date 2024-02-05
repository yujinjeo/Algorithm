n,m=map(int,input().split())

def back(dpt, picked):
  if dpt==m:
    print(*picked)
    return
  for i in range(n):
    if i+1 not in picked:
      picked.append(i+1)
      back(dpt+1,picked)
      picked.pop()

for i in range(n):
  picked=[i+1]
  back(1, picked)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 진실을 아는 사람 목록
know = set()
lst = list(map(int, input().split()))

for i in range(lst[0]):  # lst[0]은 진실을 아는 사람의 수
    know.add(lst[i+1])   # 진실을 아는 사람 추가

parties = []  # 파티 정보 저장
for i in range(m):
    tmp = list(map(int, input().split()))
    parties.append(set(tmp[1:]))  # 집합으로 저장하여 탐색 속도 증가

# 🔄 진실 전파 (BFS 방식)
changed = True
while changed:
    changed = False
    for party in parties:
        if know & party:  # 진실을 아는 사람이 포함된 파티
            if not party.issubset(know):  # 아직 다 추가되지 않은 경우
                know.update(party)
                changed = True  # 새롭게 추가됨을 표시

# ❌ 거짓말 가능한 파티 개수 카운트
ans = 0
for party in parties:
    if not (party & know):  # 진실을 아는 사람이 없는 경우만 카운트
        ans += 1

print(ans)

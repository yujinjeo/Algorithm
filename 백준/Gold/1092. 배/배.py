import sys
import heapq

input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)  # 내림차순 정렬 (가장 강한 크레인부터)

m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)  # 내림차순 정렬 (가장 무거운 박스부터)

# 가장 강한 크레인도 못 드는 박스가 존재하면 -1 출력 후 종료
if cranes[0] < boxes[0]:
    print(-1)
    sys.exit()

ans = 0
while boxes:
    i = 0  # 크레인 인덱스
    j = 0  # 박스 인덱스
    while i < n and j < len(boxes):
        if cranes[i] >= boxes[j]:  # 크레인이 박스를 들 수 있는 경우
            boxes.pop(j)  # 박스를 제거
            i += 1  # 다음 크레인으로 이동
        else:
            j += 1  # 크레인이 들 수 없으면 다음 박스 확인

    ans += 1

print(ans)

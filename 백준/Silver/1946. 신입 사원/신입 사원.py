import sys
input = sys.stdin.readline

T = int(input().strip())  # 테스트 케이스 수

for _ in range(T):
    N = int(input().strip())  # 지원자 수
    candidates = []
    
    # 지원자 정보 입력
    for _ in range(N):
        doc, interview = map(int, input().split())
        candidates.append((doc, interview))
    
    # 서류 성적 기준 오름차순 정렬
    candidates.sort()
    
    # 면접 순위 추적
    selected = 0
    min_interview_rank = float('inf')
    
    for doc, interview in candidates:
        # 현재 면접 성적이 최소값보다 낮으면 선발
        if interview < min_interview_rank:
            selected += 1
            min_interview_rank = interview  # 최소 면접 순위 갱신
    
    print(selected)

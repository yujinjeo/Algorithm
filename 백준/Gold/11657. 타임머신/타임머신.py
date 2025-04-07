import sys

input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())
edges=[]
distance = [INF]*(v+1)

for _ in range(e):
    a,b,c=map(int,input().split())
    edges.append((a,b,c))

def bellman_ford(start):
    # 시작 노드 초기화
    distance[start]=0
    # 전체 v-1 번의 라운드를 반복 : 왜? 그래프에 있는 최장 경로가 최대 v-1 개의 간선을 가질 수 있기 때문에 v 번을 반복해서 최대 간선까지 검사할 수 있도록 한다. 이어질 수 있도록 가능성 열어둠.
    for i in range(v):
        # 매 반복마다 '모든 간선'을 확인한다.
        for j in range(e):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node]+edge_cost:
                distance[next_node] = distance[cur_node]+edge_cost
                # v번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i== v-1:
                    return True
    return False

negative_cycle = bellman_ford(1)

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 노드 최단 거리 출력
    for i in range(2, v+1):
        if distance[i]==INF:
            print("-1")
        else:
            print(distance[i])
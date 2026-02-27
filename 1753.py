'''
---- 다익스트라 (시작노드번호) ----
0) import heapq

1) heapq를 사용하기 위해 q = [ ] 리스트 생성

2) heapq.heappush(q, value)

value 부분에 시작노드이므로 거리는 (0, 시작노드번호)를 함께 묶어서 힙큐에 넣어준다.

3) 최단거리테이블[시작노드] = 0 으로 초기화

4) q가 빌때까지 반복

-- heapq.heappop(q) : 큐에서 거리(dist), 노드번호(now)를 꺼낸다.

-- 만약에 꺼낸 거리값이 최단거리테이블( distance[꺼낸 노드번호] ) 에 기록된 정보보다 값이 크면, 최단거리 정보가 아니기 때문에 continue 로 무시한다.

 
-- 그게 아니라면 최단거리 정보이므로 다음과 같은 작업을 수행한다.

-- for i in graph[꺼낸노드번호]:

  꺼낸노드번호에서 갈수 있는 노드와 거리정보를 i를 통해 한개씩 접근

   >> i[0] : 현재 노드에서 갈 수 있는 노드 번호

   >> i[1] : 현재 노드에서 갈 수 있는 노드 번호까지의 거리

i[0]까지의 최소비용(cost)은 >>> 현재 노드의 최소비용(dist) + i[1]  이다.

만약에 cost값이 최단 거리 테이블의 거리정보보다 작으면, 업데이트 해주고 힙큐에 정보를 넣어준다. 

이과정을 반복하면 방문할 수 있는 노드에 대하여 최단거리테이블이 모두 갱신된다.

'''

import sys, heapq

input = sys.stdin.readline
INF = (1e9)

def dijkstra(strat_node):
    heap_arr = []
    heapq.heappush(heap_arr, (0,strat_node))
    distance[start_node] = 0

    while heap_arr:
        dist, now = heapq.heappop(heap_arr)
        if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        else: # 이러면 최단 거리임(같거나 큰 경우는 처리 안된것과 처리되어 지금 들어온 값)
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(heap_arr, (cost, i[0]))

V, E = map(int, input().split())

start_node = int(input()) #시작 노드

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1) #최단 거리 테이블

for i in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

dijkstra(start_node)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


'''
방향성이 없는 그래프가 주어진다. 
세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 
또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.
'''

import sys, heapq

input = sys.stdin.readline

INF = 1e9

def dijkstra(start):
    distance = [INF] * (N+1)
    heap_arr = []
    heapq.heappush(heap_arr,(0,start))
    distance[start] = 0

    while heap_arr:
        dist, now = heapq.heappop(heap_arr)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap_arr, (cost, i[0]))
    return distance

N, E = map(int, input().split())

graph = [[] for i in range(N+1)]

for i in range(E):
    a, b, c = map(int, input().split())
    # 방향 없으므로 두개 넣어줌
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())

# 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

'''
반드시 지나야 하는 점이 v1, v2 두 개면,
1번에서 출발해서 N번까지 갈 때 가능한 순서는:

1 -> v1 -> v2 -> N

1 -> v2 -> v1 -> N
이 두개 중 작은 길이인것을 택할 것임.

1 -> v1 -> v2 -> N 과 같은 경우
v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[N]

이건 세 구간을 더한 것:

original_distance[v1]
= 1에서 v1까지 최단거리

v1_distance[v2]
= v1에서 v2까지 최단거리

v2_distance[N]
= v2에서 N까지 최단거리
'''

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[N]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[N]

result = min(v1_path, v2_path)
print(result if result < INF else -1)
'''
문제 설명
n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

제한사항
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
입출력 예
n	vertex	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3

# 다익스트라 버전
import heapq

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    INF = int(1e9)
    dist = [INF] * (n + 1)
    dist[1] = 0

    heap = []
    heapq.heappush(heap, (0, 1))  # 거리, 노드

    while heap:
        now_dist, now_node = heapq.heappop(heap)

        # 이미 더 짧은 거리로 처리된 적 있으면 무시
        if dist[now_node] < now_dist:
            continue

        for next_node, cost in graph[now_node]:
            new_dist = now_dist + cost

            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    # 0번 인덱스 제외
    max_dist = max(dist[1:])

    return dist[1:].count(max_dist)
'''

from collections import deque

def bfs(n, graph, start):
    que = deque()
    que.append(start)
    visited = [0]*(n+1)
    visited[start] = 1
    
    while que:
        now_node = que.popleft()
        for connected_node in graph[now_node]:
            if visited[connected_node] == 0:
                que.append(connected_node)
                visited[connected_node] = visited[now_node] + 1
                
    return visited.count(max(visited))


def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    return bfs(n, graph, 1)

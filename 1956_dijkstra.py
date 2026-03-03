import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    dist_arr = [INF] * (V + 1)
    dist_arr[start] = 0
    heap_arr = [(0, start)]

    while heap_arr:
        cur_dist, now = heapq.heappop(heap_arr)

        if cur_dist > dist_arr[now]:
            continue

        # 이미 현재 답보다 크거나 같으면 더 볼 필요가 거의 없음 -> 이것이 어찌보면 핵심일지도.
        if cur_dist >= answer:
            continue

        for nxt, w in graph[now]:
            new_dist = cur_dist + w
            if new_dist < dist_arr[nxt] and new_dist < answer:
                dist_arr[nxt] = new_dist
                heapq.heappush(heap_arr, (new_dist, nxt))

    return dist_arr

V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
rev_graph = [[] for _ in range(V + 1)]

# edges = [dict() for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    rev_graph[b].append((a, c))

answer = INF

for start in range(1, V + 1):
    # start로 들어오는 간선이 없으면 사이클 불가 -> 이것 처내는것도 시간 줄이기 위해서. 
    if not rev_graph[start]:
        continue

    dist = dijkstra(start)

    for v, cost in rev_graph[start]:
        if dist[v] != INF:
            cand = dist[v] + cost
            if cand < answer:
                answer = cand

print(answer if answer != INF else -1)
'''
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다. 출발 도시와 도착 도시도 포함한다.

셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다. 경로가 여러가지인 경우 아무거나 하나 출력한다.

경로 있으니까 다익스트라 쓰면 될거고 그 과정에서 prev 두어서 역추적 해서 과정 출력하도록 하면 될듯.
'''
import sys, heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, end):
    heap_arr = []
    dist = [INF]*(N+1)
    prev = [0]*(N+1)
    heapq.heappush(heap_arr, (0,start))
    dist[start] = 0

    while heap_arr:
        weight, node = heapq.heappop(heap_arr)
        if weight > dist[node]: # 방문 했던 것이면 지나감
            continue
        for nxt, w in graph[node]:
            cost = w + weight
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(heap_arr, (cost,nxt))
                prev[nxt] = node

    return prev, dist


if __name__ == "__main__":
    N = int(input())
    M = int(input())

    graph = [[] for i in range(N+1)]

    for i in range(M):
        a, b, w = map(int,input().split())
        graph[a].append((b,w))

    start, end = map(int, input().split())
    prev_arr, dist_arr = dijkstra(start, end)
    print(dist_arr[end])
    cnt = 1 # 미리 end 는 넣고 시작하니까 cnt 가 1로 시작하는것임. 
    cursor = end
    result_arr = [end]
    while cursor != start:
        result_arr.append(prev_arr[cursor])
        cursor = prev_arr[cursor]
        cnt += 1
    result_arr.reverse()
    print(cnt)
    print(*result_arr)
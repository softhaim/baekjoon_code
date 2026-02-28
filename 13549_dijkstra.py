'''
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
'''

'''
예전에 이런 문제를 bfs로 푼적이 있었는데, dijkstra로도 풀 수 있나봄.
일반 BFS는 “먼저 들어온 것”부터 처리하는데,
이 문제는 더 늦게 들어왔더라도 비용이 더 작은(0초) 경로가 있을 수 있음.

그래서 이 문제는:

0-1 BFS (deque에서 0비용은 appendleft) -> 115096kb	128ms
하거나 
다익스트라 -> 117408kb	228ms
'''

import sys, heapq
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    dist = [INF]*(max_n+1)
    heap_arr = []
    heapq.heappush(heap_arr, (0, start))
    dist[start] = 0

    while heap_arr:
        time, now = heapq.heappop(heap_arr)
        if dist[now] < time: # 이미 처리한 내용은 패스
            continue
        if now == end:
            return time
        '''
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap_arr, (cost, i[0]))
        평소에 하던 이것은 그래프 받은거 기반해서 연결된 것 순회하면서 cost측정하고 이 코스트가 새로 연결하거나, 기존보다 싸면 연결하는 것
        여기서는 저 cost가 time이고 순간이동은 0 이고 다른건 1인것임. 노드는 2*x, x-1, x+1
        '''
        # 순간이동 - 0초
        nx = now*2
        if 0 <= nx <= max_n and time < dist[nx]:
            dist[nx] = time
            heapq.heappush(heap_arr, (time,nx))
        
        # 걷기
        for nx in (now-1, now+1):
            if 0<= nx <= max_n and time < dist[nx]:
                dist[nx] = time + 1
                heapq.heappush(heap_arr, (time+1, nx))

    return dist[end]


if __name__ == "__main__":
    N, K = map(int, input().split())

    max_n = 100000

    print(dijkstra(N, K))


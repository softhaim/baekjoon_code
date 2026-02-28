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

0-1 BFS (deque에서 0비용은 appendleft)
하거나 
다익스트라
'''

import sys, heapq
from collections import deque

input = sys.stdin.readline

def bfs(start, end):
    queue = deque()
    queue.append(start)
    
    while queue:
        nx = queue.popleft()
        if nx == end:
            return
        for x in (nx-1,nx+1,2*nx):
            if x == start or not(0<=x<=max_n):
                continue
            if graph[x] == 0:
                if x == 2*nx: # 더 늦게 들어왔어도 비용이 이게 더 작을 수 있으니 이것부터 보는것임. 텔포는 0이니까.
                    graph[x] = graph[nx]
                    queue.appendleft(x)
                else:
                    graph[x] = graph[nx] + 1
                    queue.append(x)
    return

if __name__ == "__main__":
    N, K = map(int, input().split())

    max_n = 100000

    graph = [0]*(max_n+1)

    bfs(N,K)

    print(graph[K])

#14940

'''
지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)

다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

출력
각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 
갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.
'''

import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, visited, start):
    # 상하좌우 탐색
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([start])
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1: # 범위 안에 있고, 방문하지 않았다면
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
        
n, m  = map(int, input().split())
graph = [[0] *m for _ in range(n)]
visited = [[-1] *m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i,j)
        elif graph[i][j] == 0:
            visited[i][j] = 0

bfs(graph, visited, start)

for i in range(n):
    for j in range(m):
        print(visited[i][j], end=' ')
    print()


'''
전형적인 BFS 의 경로찾기 문제에 벽을 부술 수 있다는 특징이 포함된 문제이다.

중간에 벽을 단 한번만 부술 수 있기 때문에 벽을 부쉈는지의 여부를 3차원 행렬로써 나타내면 된다.

벽 부수기 없이 나타낸다면 visit[x][y] 라고 표현할 수 있지만 z를 추가함으로써 0은 안부숨, 1은 부숨을 표현할 수 있다.

즉, visited[0][x][y]은 안부순 경로, visited[1][x][y]은 부순 경로.
if graph[x][y] == 1 and c == 0 이게 벽인데 아직 벽 부수기 안한 경로 분기 일것임.



'''

import sys 
from collections import deque

input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b,map_arr,visited,N,M):
    queue = deque()
    queue.append((a,b,0))

    visited[0][a][b] = 1

    while queue:
        nx, ny, nz = queue.popleft()
        if nx == N-1 and ny == M-1:
            return visited[nz][nx][ny]
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if not(0<=x<N and 0<=y<M): continue
            if map_arr[x][y] == 1 and nz == 0: # 아직 벽 안부순 경우
                visited[1][x][y] = visited[0][nx][ny] + 1
                queue.append((x,y,1))
            elif map_arr[x][y] == 1 and nz == 1: continue
            elif map_arr[x][y] == 0 and visited[nz][x][y] == 0:
                visited[nz][x][y] = visited[nz][nx][ny] + 1
                queue.append((x,y,nz))
    return -1

def main():

    N, M = map(int,input().split())

    map_arr = []

    for i in range(N):
        input_num = list(map(int,input().strip()))
        map_arr.append(input_num)

    visited = [[[0]*M for _ in range(N)] for _ in range(2)]

    print(bfs(0,0, map_arr, visited, N, M))

if __name__ == "__main__":
    main()
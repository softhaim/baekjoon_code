'''
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

'''

'''
미로의 1을 방문하면 여기서 bfs 써서 탐색하고 이전 경로의 값에서 +1 씩하면서 이동한 값을 기록하도록 함. 
그렇게 1인데만 탐색하면서 이동한 값 기록하고 그렇게 도착했을때 이동한 값 마지막 위치에 저장하도록 하고 출력

'''

import sys
from collections import deque 

input = sys.stdin.readline

N, M = map(int, input().split())

map_arr = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(N):
    input_map = list(map(int,input().strip()))
    map_arr.append(input_map)

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    # map_arr[a][b] = 1 # 처음 들어간 곳이라서 1원래는 해주긴 해야하는데 어차피 맵에서 1이니까 걍 냅둠

    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if x < 0 or x >= N or y < 0 or y >= M or (x==0 and y==0): # 마지막에 저 0,0 은 시작이니까 다시 탐색하지 않도록 해줌. 그냥 두면 1 이라서 다시 탐색할거라서 시작 부분.
                continue
            elif map_arr[x][y] == 1:
                map_arr[x][y] = map_arr[nx][ny] + 1
                queue.append((x,y))
    return
bfs(0,0)
print(map_arr[N-1][M-1])
'''
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
'''

import sys
from collections import deque

input = sys.stdin.readline

N = int(input()) # 문제의 수를 입력 받음

# 여기서는 이동할 수 있는 좌표 리스트 순차적으로 가능한 좌표 넣을 것임.
dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]

# 전형적인 bfs, 여기서 목적지면 return 해서 불필요한 연산 없이 종료하고, 탐색하는 곳은 이전의 수에서 +1 해주면서 지금 몇번째 이동인지 map_arr 에 기록.
def bfs(start,end,map_arr,L):
    queue = deque()
    queue.append(start)

    while queue:
        nx, ny = queue.popleft()
        if nx == end[0] and ny == end[1]:
            return
        for i in range(8):
            x = nx + dx[i]
            y = ny + dy[i]
            if not (0<=x<L and 0<=y<L):
                continue
            elif x == end[0] and y == end[1]:
                map_arr[x][y] = 1 + map_arr[nx][ny]
                return
            elif map_arr[x][y] == 0:
                map_arr[x][y] = 1 + map_arr[nx][ny]
                queue.append((x,y))
    return 

# 테스트 수 만큼 받으면서 반복해서 문제 받고 해결
for i in range(N):
    L = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    map_arr = [[0]*(L) for _ in range(L)] # L +1 로 하니까 틀렸다 뜸. 이거 고치니까 맞음.
    bfs(start, end, map_arr, L)
    print(map_arr[end[0]][end[1]])

    
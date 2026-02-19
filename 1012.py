'''

배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 
예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

1	1	0	0	0	0	0	0	0	0
0	1	0	0	0	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	1	1	0	0	0	1	1	1
0	0	0	0	1	0	0	1	1	1

'''

'''
이 문제는 graph 방문 했던 곳을 0 으로 두면서 1인 데 만나면, 들어가서 bfs 든 dfs든 해서 한번 전체 탐색 하고 나서 1씩 카운트를 추가하면 된다.
들어가서 1인데를 다 탐색하면서 탐색했던데는 0 으로 만듦. 그렇게 해서 한번 탐색한데는 지나치고 그렇게 탐색한 곳을 한번에 1씩 카운트 해서 저장해두고 출력하면 이 문제를 풀 수 있음 약간 2667 문제와 비슷
'''

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b):
    queue = deque()
    queue.append((a,b)) # a,b의 좌표를 큐에 입력
    baechu_map[a][b] = 0 # 현재 방문 했으니까 0 으로 만들어 줌

    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if x < 0 or x >= N or y < 0 or y >= M: continue
            if baechu_map[x][y] == 1:
                queue.append((x,y))
                baechu_map[x][y] = 0
    return 

count_arr = [0]*T
for test in range(T):
    M, N, K = map(int, input().split())
    baechu_map = [[0]*M for _ in range(N)]

    for i in range(K):
        baechu_x, baechu_y = map(int, input().split())
        baechu_map[baechu_y][baechu_x] = 1

    for i in range(N): # N 이 세로라서 행
        for  j in range(M): # M이 가로이니까 열임
            if baechu_map[i][j] == 1:
                bfs(i,j)
                count_arr[test] += 1

for val in count_arr:
    print(val)
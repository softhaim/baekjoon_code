'''
창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 
토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''

'''
bfs로 인접한거 상하좌우 넣으면서 이전 값기반으로 +1 하면서 넣고 이를 1인 지점별(시작 지점)로 체크를 함. 
여기서 핵심은 bfs 로 처음 시작위치를 전부 넣는것임. 그렇게 모든 시작위치에서 bfs하면서 기록함.
만약 최종에서 0이 존재한다면 그것은 전부 익은거 아니니까 -1해야함.
또한 입력 받은 값에서 0이 없다면 0 출력해야함.
'''

import sys
from collections import deque

input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(queue:deque, input_map ):
    N = len(input_map)
    M = len(input_map[0]) if N > 0 else 0  # 빈 맵 방어

    for val in queue:
        input_map[val[0]][val[1]] = 0

    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            x = dx[i] + nx
            y = dy[i] + ny

            if not(0<=x<N and 0<=y<M): continue
            elif input_map[x][y] == 0:
                input_map[x][y] = input_map[nx][ny] + 1
                queue.append((x,y))
    return

def main():

    M, N = map(int, input().split())

    map_arr = []
    start_index = deque()

    for i in range(N):
        input_num = list(map(int, input().split()))
        pos = [i for i, v in enumerate(input_num) if v == 1]
        map_arr.append(input_num)
        for val in pos: start_index.append((i,val))

    if all(0 not in row for row in map_arr):
        print(0)
        exit(0)

    bfs(start_index, map_arr)

    if any(0 in row for row in map_arr):
        print(-1)
        exit(0)

    mx = max(v for row in map_arr for v in row)
    print(mx)


if __name__ == "__main__":
    main()
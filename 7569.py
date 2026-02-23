'''
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''

'''
3 차원으로 배열을 받고 3차원을 기준으로 bfs하면서 시작위치 넣고 하면 됨.
근데 여기서 map[z][x][y] 으로 접근해야하고 이에 따른 입력 잘 구성해서 넣고, 스타드 인덱스도 튜플로 잘 넣어두고 이를 bfs 큐로 넘겨줌.
그럼 시작 위치 기반으로 너비 탐색하면서 그 위치까지 이동하는데 걸린 최솟값을 잘 기록 할 것임. 그렇게 기록하고 최대값 출력하게 하면 얼마나 최대 걸리는 지 파악가능.
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다. 입력 이후에 0 없으면 0 출력 하고 bfs이후에도 0 이 남았다면 -1 출력.
'''

from collections import deque
import sys

input = sys.stdin.readline

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs(queue:deque, input_map, n, m, h):

    while queue:
        nx, ny, nz = queue.popleft()
        for i in range(6):
            x = nx + dx[i]
            y = ny + dy[i]
            z = nz + dz[i]
            if not(0<=x<n and 0<=y<m and 0<=z<h): continue
            elif input_map[z][x][y] == 0:
                input_map[z][x][y] = input_map[nz][nx][ny] + 1
                queue.append((x,y,z))

    return

def main():
    M, N, H = map(int, input().split())

    map_arr = [[] for i in range(H)]
    start_index = deque()

    for j in range(H):
        for i in range(N):
            input_num = list(map(int, input().split()))
            pos = [idx for idx, v in enumerate(input_num) if v == 1]
            map_arr[j].append(input_num)
            for val in pos: start_index.append((i,val,j))
             
    if all(0 not in row for box in map_arr for row in box): # 토마토 다 익어이는 상태
        print(0)
        exit(0)

    bfs(start_index, input_map=map_arr, m=M, n=N, h=H)

    if any(0 in row for box in map_arr for row in box):
        print(-1)
        exit(0)
    
    mx = max(v for box in map_arr for row in box for v in row)
    print(mx-1) # 시작 위치가 1 이라서 1일 후가 2, 2일 후가 3 이런식으로 +1 된 상황이라 출력은 -1 해주는 것임.
    

if __name__ == "__main__":
    main()
'''
주사위를 굴려 나온 수가 4라면, i+4번 칸으로 이동해야 한다. 만약 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없다. 
도착한 칸이 사다리면, 사다리를 타고 위로 올라간다. 뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 된다. 
즉, 사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크고, 뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작아진다.

게임의 목표는 1번 칸에서 시작해서 100번 칸에 도착하는 것이다.

게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값을 구해보자.
'''

'''
이것도 bfs를 통해서 시작값 넣고 탐색하는데 핵심은 사다리 및 뱀을 입력 받아서 이를 저장하고 딕셔너리로 시작값 입력되면 그걸 기반으로 이동하는 위치 값하도록 저장.
이를 기반으로 이 딕셔너리안의 값이면 그 값으로 변경하고 그 값 기반으로 bfs 하도록 함. 
x = nx + dx 에서 x 가 dict 에 있으면 그 값으로 x 바꾸고 queue(x) 하는거임 이동거리는 출발위치 값 + 1을 저 new_x위치에 저장.
'''

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, map_arr, move):
    queue = deque()
    queue.append(start)

    map_arr[start] = 0

    while queue:
        pos = queue.popleft()
        for i in range(6,0,-1):
            next_pos = pos + i
            if not(1<=next_pos<=100): continue
            if next_pos in move:
                next_pos = move[next_pos]
            if next_pos == 100:
                map_arr[next_pos] = map_arr[pos] + 1
                return
            if map_arr[next_pos] == 0:
                map_arr[next_pos] = map_arr[pos] + 1
                queue.append(next_pos)
    return

def main():
    N, M = map(int, input().split())

    map_arr = [0]*101

    stair = []

    for i in range(N): # 사다라 밭음. 작은거 -> 큰거
        x, y = map(int, input().split())
        if x > y: stair.append((y,x))
        else: stair.append((x,y))

    for i in range(M): # 뱀 받음. 큰거 -> 작은거
        x, y = map(int, input().split())
        if x > y: stair.append((x,y))
        else: stair.append((y,x))

    move = dict(stair)

    bfs(1, map_arr, move)

    print(map_arr[100])

if __name__ == "__main__":
    main()
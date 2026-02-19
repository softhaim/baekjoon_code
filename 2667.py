'''
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. 
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
'''
'''
1인 지점에서 탐색을 시작합니다.

탐색 중 1인 부분은 0으로 바꿔 다시 방문하지 않도록 하고

한 번의 BFS가 끝나게 되면 더 이상 확장이 불가능 하므로 마을 하나가 탄생합니다.

이 마을안의 1의 개수들을 출력하면 되므로 다음 코드와 같이 count를 반환하면 됩니다.
'''
import sys 
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())

graph = []
count_arr = []

def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0 # 방문 했으니까 0으로 해줌
    count = 1
    while queue:
        nx, ny = queue.popleft()
        # print(v)
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if x < 0 or x >= N or y < 0 or y >= N: continue
            if graph[x][y] == 1:
                queue.append((x,y))
                graph[x][y] = 0
                count += 1
    return count

for i in range(N):
    input_map = list(map(int, input().strip()))
    graph.append(input_map)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count_arr.append(bfs(i,j))

count_arr.sort()
print(len(count_arr))

for val in count_arr:
    print(val)
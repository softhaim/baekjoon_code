'''
다리의 양 끝은 섬과 인접한 바다 위에 있어야 하고, 한 다리의 방향이 중간에 바뀌면 안된다. 또, 다리의 길이는 2 이상이어야 한다.

다리의 방향이 중간에 바뀌면 안되기 때문에, 다리의 방향은 가로 또는 세로가 될 수 밖에 없다. 방향이 가로인 다리는 다리의 양 끝이 가로 방향으로 섬과 인접해야 하고, 방향이 세로인 다리는 다리의 양 끝이 세로 방향으로 섬과 인접해야 한다.

bfs 써서 섬 분별하고 크루스칼로 MST하면 되는 문제인데, 간선을 찾는것이 접근이 어려웠다. 이동하려는 곳이 1. 자기 자신 섬인 경우, 2. 이동하는데가 바다인경우, 3. 다른섬 만난 경우 이걸 다 고려해야해서 이게 힘들었다.
'''
import sys
from collections import deque

input = sys.stdin.readline
INF = float('inf')

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def get_edge():
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0: # 섬이면
                island = board[i][j]

                for d in range(4):
                    ni, nj = i+dy[d], j+dx[d]
                    length = 0
                    while 0 <= ni < N and 0<= nj < M:
                        if board[ni][nj] == island: # 이동하려는데가 자기 자신의 섬 내부
                            break
                        if board[ni][nj] == 0: # 이동하려는데가 바다 -> 현재 진행 방향으로 계속 감
                            length += 1
                            ni += dy[d]
                            nj += dx[d]
                            continue
                        else:
                            if length > 1: # board[ni][nj] != island and board[ni][nj] != 0 -> 다른 섬 만난 경우인데 길이 1 이상이면,
                                other = board[ni][nj]
                                # 같은 두 섬 사이의 여러 간선 중에서는 최소 비용 간선 하나만 남겨도 MST 결과가 바뀌지 않음. -> 다 저장해봐야 시간복잡도만 늘어나니 최소만 저장
                                dist[island][other] = min(dist[island][other], length)
                                dist[other][island] = min(dist[other][island], length)
                            break
    return

def bfs(x,y,mark):
    que = deque()
    que.append((x,y))
    visited[x][y] = True
    board[x][y] = mark

    while que:
        now_i, now_j = que.popleft()
        for i in range(4):
            next_j = now_j + dx[i]
            next_i = now_i + dy[i]
            if 0<= next_j< M and 0<= next_i < N and visited[next_i][next_j] == False and board[next_i][next_j]:
                visited[next_i][next_j] = True
                que.append((next_i, next_j))
                board[next_i][next_j] = mark

    return

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
    return

if __name__ == "__main__":
    N, M = map(int, input().split()) # 세로, 가로
    visited = [[False]*(M) for _ in range(N)]
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    # 맵에 섬마다 bfs를 통하여 인접한 1 인것 같은 숫자로 마킹
    mark = 1
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and board[i][j]:
                bfs(i,j,mark)
                mark += 1
    
    # 마킹 해둔거 바탕으로 간선 찾음
    dist = [[INF]*(mark) for _ in range(mark)] # 각 섬들끼리 최소 거리 저장 리스트
    get_edge()

    edge = []
    for i, row in enumerate(dist):
        for j, val in enumerate(row):
            if val != INF:
                edge.append((val, i, j))
    edge.sort()
    
    # 구한 간선으로 MST
    result = 0
    cnt = 0 # 간선 개수가 노드 개수 -1 인지 판단하여 다 이어졌는지 체크하기 위한 변수
    parent = [i for i in range(mark)]
    for c, i, j in edge:
        if find(i) != find(j):
            union(i, j)
            result += c
            cnt += 1

    if cnt == mark-2: # mark 는 1-index 때문에 +1 더 되어있는 상황. 간선 개수 = 노드 개수 -1 이라 mark-2임.
        print(result)
    else:
        print(-1)
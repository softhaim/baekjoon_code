
'''
bfs로 석유의 위치 찾으면서 개수 누적하고 해당 수 만큼 퍼져있는 컬럼의 위치에 개수만큼 + 해서 저장해둠.
이렇게 해서 해당 석유가 퍼져있는 컬럼에 대해서는 해당 석유를 캘 수 있으니 전부 + 해줌으로써 가장 많은 수 시추 가능한 컬럼만 찾으면 됨.

문제 설명
[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]

세로길이가 n 가로길이가 m인 격자 모양의 땅 속에서 석유가 발견되었습니다. 석유는 여러 덩어리로 나누어 묻혀있습니다. 당신이 시추관을 수직으로 단 하나만 뚫을 수 있을 때, 가장 많은 석유를 뽑을 수 있는 시추관의 위치를 찾으려고 합니다. 시추관은 열 하나를 관통하는 형태여야 하며, 열과 열 사이에 시추관을 뚫을 수 없습니다.

석유시추-1.drawio.png

예를 들어 가로가 8, 세로가 5인 격자 모양의 땅 속에 위 그림처럼 석유가 발견되었다고 가정하겠습니다. 상, 하, 좌, 우로 연결된 석유는 하나의 덩어리이며, 석유 덩어리의 크기는 덩어리에 포함된 칸의 수입니다. 그림에서 석유 덩어리의 크기는 왼쪽부터 8, 7, 2입니다.

석유시추-2.drawio.png

시추관은 위 그림처럼 설치한 위치 아래로 끝까지 뻗어나갑니다. 만약 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있습니다. 시추관이 뽑을 수 있는 석유량은 시추관이 지나는 석유 덩어리들의 크기를 모두 합한 값입니다. 시추관을 설치한 위치에 따라 뽑을 수 있는 석유량은 다음과 같습니다.

시추관의 위치	획득한 덩어리	총 석유량
1	[8]	8
2	[8]	8
3	[8]	8
4	[7]	7
5	[7]	7
6	[7]	7
7	[7, 2]	9
8	[2]	2
오른쪽 그림처럼 7번 열에 시추관을 설치하면 크기가 7, 2인 덩어리의 석유를 얻어 뽑을 수 있는 석유량이 9로 가장 많습니다.

석유가 묻힌 땅과 석유 덩어리를 나타내는 2차원 정수 배열 land가 매개변수로 주어집니다. 이때 시추관 하나를 설치해 뽑을 수 있는 가장 많은 석유량을 return 하도록 solution 함수를 완성해 주세요.

제한사항
1 ≤ land의 길이 = 땅의 세로길이 = n ≤ 500
1 ≤ land[i]의 길이 = 땅의 가로길이 = m ≤ 500
land[i][j]는 i+1행 j+1열 땅의 정보를 나타냅니다.
land[i][j]는 0 또는 1입니다.
land[i][j]가 0이면 빈 땅을, 1이면 석유가 있는 땅을 의미합니다.
정확성 테스트 케이스 제한사항
1 ≤ land의 길이 = 땅의 세로길이 = n ≤ 100
1 ≤ land[i]의 길이 = 땅의 가로길이 = m ≤ 100
효율성 테스트 케이스 제한사항
주어진 조건 외 추가 제한사항 없습니다.
입출력 예
land	result
[[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]	9
[[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]	16
'''
from collections import deque

def bfs(land, si, sj, visited, oil_by_col, numbering):
    que = deque()
    que.append((si, sj))
    visited[si][sj] = numbering
    cols = set()
    oil_col = 0
    while que:
        i, j = que.popleft()
        cols.add(j)
        oil_col += 1
        
        for di, dj in ((0,1), (0,-1),(1,0),(-1,0)):
            ni = di + i
            nj = dj + j
            if (0<=ni<len(land) 
                and 0<=nj<len(land[0]) 
                and land[ni][nj] == 1 
                and visited[ni][nj] == 0):
                visited[ni][nj] = numbering
                que.append((ni,nj))
    
    for col in cols:
        oil_by_col[col] += oil_col
    
    return 1

def solution(land):
    numbering = 1
    visited = [[0]*(len(land[0])) for _ in range(len(land))]
    oil_by_col = [0] * len(land[0])
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 0 or visited[i][j] != 0:
                continue
            numbering += bfs(land, i, j, visited, oil_by_col, numbering)
            
    return max(oil_by_col)
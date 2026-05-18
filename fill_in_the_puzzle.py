'''
문제 설명
테이블 위에 놓인 퍼즐 조각을 게임 보드의 빈 공간에 적절히 올려놓으려 합니다. 게임 보드와 테이블은 모두 각 칸이 1x1 크기인 정사각 격자 모양입니다. 이때, 다음 규칙에 따라 테이블 위에 놓인 퍼즐 조각을 게임 보드의 빈칸에 채우면 됩니다.

조각은 한 번에 하나씩 채워 넣습니다.
조각을 회전시킬 수 있습니다.
조각을 뒤집을 수는 없습니다.
게임 보드에 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안 됩니다.
다음은 퍼즐 조각을 채우는 예시입니다.

puzzle_5.png

위 그림에서 왼쪽은 현재 게임 보드의 상태를, 오른쪽은 테이블 위에 놓인 퍼즐 조각들을 나타냅니다. 테이블 위에 놓인 퍼즐 조각들 또한 마찬가지로 [상,하,좌,우]로 인접해 붙어있는 경우는 없으며, 흰 칸은 퍼즐이 놓이지 않은 빈 공간을 나타냅니다. 모든 퍼즐 조각은 격자 칸에 딱 맞게 놓여있으며, 격자 칸을 벗어나거나, 걸쳐 있는 등 잘못 놓인 경우는 없습니다.

이때, 아래 그림과 같이 3,4,5번 조각을 격자 칸에 놓으면 규칙에 어긋나므로 불가능한 경우입니다.

3번 조각을 놓고 4번 조각을 놓기 전에 위쪽으로 인접한 칸에 빈칸이 생깁니다.
5번 조각의 양 옆으로 인접한 칸에 빈칸이 생깁니다.
다음은 규칙에 맞게 최대한 많은 조각을 게임 보드에 채워 넣은 모습입니다.

puzzle_7.png

최대한 많은 조각을 채워 넣으면 총 14칸을 채울 수 있습니다.

현재 게임 보드의 상태 game_board, 테이블 위에 놓인 퍼즐 조각의 상태 table이 매개변수로 주어집니다. 규칙에 맞게 최대한 많은 퍼즐 조각을 채워 넣을 경우, 총 몇 칸을 채울 수 있는지 return 하도록 solution 함수를 완성해주세요.

제한사항
3 ≤ game_board의 행 길이 ≤ 50
game_board의 각 열 길이 = game_board의 행 길이
즉, 게임 보드는 정사각 격자 모양입니다.
game_board의 모든 원소는 0 또는 1입니다.
0은 빈칸, 1은 이미 채워진 칸을 나타냅니다.
퍼즐 조각이 놓일 빈칸은 1 x 1 크기 정사각형이 최소 1개에서 최대 6개까지 연결된 형태로만 주어집니다.
table의 행 길이 = game_board의 행 길이
table의 각 열 길이 = table의 행 길이
즉, 테이블은 game_board와 같은 크기의 정사각 격자 모양입니다.
table의 모든 원소는 0 또는 1입니다.
0은 빈칸, 1은 조각이 놓인 칸을 나타냅니다.
퍼즐 조각은 1 x 1 크기 정사각형이 최소 1개에서 최대 6개까지 연결된 형태로만 주어집니다.
game_board에는 반드시 하나 이상의 빈칸이 있습니다.
table에는 반드시 하나 이상의 블록이 놓여 있습니다.
입출력 예
game_board	table	result
[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]	[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]	14
[[0,0,0],[1,1,0],[1,1,1]]	[[1,1,1],[1,0,0],[0,0,0]]	0

bfs를 각 게임보드와 table 각각 2개 bfs 해서 각각의 piece를 구하고 이 값의 좌표가 각각 다르니까 정규화를 해줌.
정규화는 가장 작은 x, y를 기준으로 x-min_x 이런식으로 해서 각각 도형을 기록해둠.
이후 game_board 의 빈칸의 모양과, piece의 빈칸 모양 다 정규화 해둔거 바탕으로 비교해서 rotate 4번해서 돌려서라도 맞으면, 맞았다 체크하고 used 에 사용했다는 것을 기록하고, answer 에 해당 도형 길이만큼 + 해서 채워진 도형 몇개인지 기록

'''

from collections import deque

def normalize(shape):
    min_y = min(y for y, x in shape)
    min_x = min(x for y, x in shape)

    normalized = []

    for y, x in shape:
        normalized.append((y - min_y, x - min_x))

    normalized.sort()
    return normalized


def bfs(arr, visited, n, start, target):
    que = deque()
    que.append(start)
    visited[start[0]][start[1]] = True

    shape = [start]

    while que:
        now_y, now_x = que.popleft()

        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            y = now_y + dy
            x = now_x + dx

            if (0 <= y < n
                and 0 <= x < n
                and not visited[y][x]
                and arr[y][x] == target):

                visited[y][x] = True
                que.append((y, x))
                shape.append((y, x))

    return normalize(shape)


def rotate(shape):
    rotated = []

    # 90도 회전: (y, x) -> (x, -y)
    for y, x in shape:
        rotated.append((x, -y))

    return normalize(rotated)


def is_match(blank, piece):
    rotated = piece

    for _ in range(4):
        if blank == rotated:
            return True
        rotated = rotate(rotated)

    return False


def solution(game_board, table):
    n = len(game_board)

    blanks = []
    pieces = []

    visited_game = [[False] * n for _ in range(n)]
    visited_table = [[False] * n for _ in range(n)]

    # game_board에서는 빈칸 0 덩어리를 찾음
    for i in range(n):
        for j in range(n):
            if not visited_game[i][j] and game_board[i][j] == 0:
                blanks.append(bfs(game_board, visited_game, n, (i, j), 0))

    # table에서는 조각 1 덩어리를 찾음
    for i in range(n):
        for j in range(n):
            if not visited_table[i][j] and table[i][j] == 1:
                pieces.append(bfs(table, visited_table, n, (i, j), 1))

    used = [False] * len(pieces)
    answer = 0

    for blank in blanks:
        for i in range(len(pieces)):
            if used[i]:
                continue

            piece = pieces[i]

            if len(piece) != len(blank):
                continue

            if is_match(blank, piece):
                used[i] = True
                answer += len(blank)
                break

    return answer
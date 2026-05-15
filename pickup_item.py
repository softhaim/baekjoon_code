'''
문제 설명
다음과 같은 다각형 모양 지형에서 캐릭터가 아이템을 줍기 위해 이동하려 합니다.

rect_1.png

지형은 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현하며, 캐릭터는 이 다각형의 둘레(굵은 선)를 따라서 이동합니다.

만약 직사각형을 겹친 후 다음과 같이 중앙에 빈 공간이 생기는 경우, 다각형의 가장 바깥쪽 테두리가 캐릭터의 이동 경로가 됩니다.

rect_2.png

단, 서로 다른 두 직사각형의 x축 좌표 또는 y축 좌표가 같은 경우는 없습니다.

rect_4.png

즉, 위 그림처럼 서로 다른 두 직사각형이 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.

다음 그림과 같이 지형이 2개 이상으로 분리된 경우도 없습니다.

rect_3.png

한 직사각형이 다른 직사각형 안에 완전히 포함되는 경우 또한 없습니다.

rect_7.png

지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때, 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return 하도록 solution 함수를 완성해주세요.

제한사항
rectangle의 세로(행) 길이는 1 이상 4 이하입니다.
rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.
직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.
서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.
charcterX, charcterY는 1 이상 50 이하인 자연수입니다.
지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
itemX, itemY는 1 이상 50 이하인 자연수입니다.
지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.
전체 배점의 50%는 직사각형이 1개인 경우입니다.
전체 배점의 25%는 직사각형이 2개인 경우입니다.
전체 배점의 25%는 직사각형이 3개 또는 4개인 경우입니다.
입출력 예
rectangle	characterX	characterY	itemX	itemY	result
[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]	1	3	7	8	17
[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]	9	7	6	1	11
[[1,1,5,7]]	1	1	4	7	9
[[2,1,7,5],[6,4,10,10]]	3	1	7	10	15
[[2,2,5,5],[1,3,6,4],[3,1,4,6]]	1	4	6	3	10


계속 실패하길래 원인을 보니 아래 예시 같은 경우 때문에 발생함.
예: 사각형의 오른쪽 변이 x=3이고, 사각형 의 왼쪽 변이 x=4일 때, 실제로는 통과할 수 없는 빈 공간임.
하지만 배열 상에서는 [y][3] 바로 옆이 [y][4]이므로, BFS 등의 탐색 시 공간을 건너뛰어 지름길로 가버리는 현상이 발생됨.
그래서 좌표를 2배 해서 풀고, 결과에서 //2 해서 반환하도록 풀어야 함.
'''

from collections import deque

def bfs(coordinate_plane, characterX, characterY, itemX, itemY, max_val):
    que = deque()
    que.append((characterX, characterY, 0))

    visited = [[False] * max_val for _ in range(max_val)]
    visited[characterY][characterX] = True

    while que:
        now_x, now_y, cnt = que.popleft()

        if now_x == itemX and now_y == itemY:
            return cnt // 2

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_x = now_x + dx
            next_y = now_y + dy

            if (0 <= next_x < max_val
                and 0 <= next_y < max_val
                and visited[next_y][next_x] == False
                and coordinate_plane[next_y][next_x] == 1):

                que.append((next_x, next_y, cnt + 1))
                visited[next_y][next_x] = True


def solution(rectangle, characterX, characterY, itemX, itemY):
    max_val = 102

    # rectangle 기반 map 설정
    coordinate_plane = [[0] * max_val for _ in range(max_val)]

    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):

                # 내부는 이동 불가
                if x1 < x < x2 and y1 < y < y2:
                    coordinate_plane[y][x] = 2

                # 테두리는 이동 가능
                else:
                    if coordinate_plane[y][x] != 2:
                        coordinate_plane[y][x] = 1

    return bfs(
        coordinate_plane,
        characterX * 2,
        characterY * 2,
        itemX * 2,
        itemY * 2,
        max_val
    )


if __name__ == "__main__":
    test_cases = [
        (
            [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]],
            1, 3,
            7, 8,
            17
        ),
        (
            [[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]],
            9, 7,
            6, 1,
            11
        ),
        (
            [[1, 1, 5, 7]],
            1, 1,
            4, 7,
            9
        ),
        (
            [[2, 1, 7, 5], [6, 4, 10, 10]],
            3, 1,
            7, 10,
            15
        ),
        (
            [[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]],
            1, 4,
            6, 3,
            10
        )
    ]

    for idx, case in enumerate(test_cases, 1):
        rectangle, characterX, characterY, itemX, itemY, gold = case

        answer = solution(rectangle, characterX, characterY, itemX, itemY)

        print(f"Test {idx}")
        print(f"ANS : {answer}")
        print(f"Gold: {gold}")
        print(f"Pass: {answer == gold}")
        print("-" * 30)
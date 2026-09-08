'''
문제 설명
각 칸마다 S, L, 또는 R가 써져 있는 격자가 있습니다. 당신은 이 격자에서 빛을 쏘고자 합니다. 이 격자의 각 칸에는 다음과 같은 특이한 성질이 있습니다.

빛이 "S"가 써진 칸에 도달한 경우, 직진합니다.
빛이 "L"이 써진 칸에 도달한 경우, 좌회전을 합니다.
빛이 "R"이 써진 칸에 도달한 경우, 우회전을 합니다.
빛이 격자의 끝을 넘어갈 경우, 반대쪽 끝으로 다시 돌아옵니다. 예를 들어, 빛이 1행에서 행이 줄어드는 방향으로 이동할 경우, 같은 열의 반대쪽 끝 행으로 다시 돌아옵니다.
당신은 이 격자 내에서 빛이 이동할 수 있는 경로 사이클이 몇 개 있고, 각 사이클의 길이가 얼마인지 알고 싶습니다. 경로 사이클이란, 빛이 이동하는 순환 경로를 의미합니다.

예를 들어, 다음 그림은 격자 ["SL","LR"]에서 1행 1열에서 2행 1열 방향으로 빛을 쏠 경우, 해당 빛이 이동하는 경로 사이클을 표현한 것입니다.

ex1.png

이 격자에는 길이가 16인 사이클 1개가 있으며, 다른 사이클은 존재하지 않습니다.

격자의 정보를 나타내는 1차원 문자열 배열 grid가 매개변수로 주어집니다. 주어진 격자를 통해 만들어지는 빛의 경로 사이클의 모든 길이들을 배열에 담아 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ grid의 길이 ≤ 500
1 ≤ grid의 각 문자열의 길이 ≤ 500
grid의 모든 문자열의 길이는 서로 같습니다.
grid의 모든 문자열은 'L', 'R', 'S'로 이루어져 있습니다.

입출력 예
grid	result
["SL","LR"]	[16]
["S"]	[1,1,1,1]
["R","R"]	[4,4]
'''

def solution(grid):
    R = len(grid)
    C = len(grid[0])
    
    # visited[r][c][d] : (r, c) 위치에서 d 방향으로 나가는/들어오는 빛의 방문 여부
    # 0: 상, 1: 우, 2: 하, 3: 좌
    visited = [[[False] * 4 for _ in range(C)] for _ in range(R)]
    
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    answer = []

    for r in range(R):
        for c in range(C):
            for d in range(4):
                if visited[r][c][d]:
                    continue
                
                count = 0
                curr_r, curr_c, curr_d = r, c, d
                
                # 사이클 추적
                while not visited[curr_r][curr_c][curr_d]:
                    visited[curr_r][curr_c][curr_d] = True
                    count += 1
                    
                    # 1. 현재 방향으로 이동
                    curr_r = (curr_r + dr[curr_d]) % R
                    curr_c = (curr_c + dc[curr_d]) % C
                    
                    # 2. 도착한 칸의 노드 타입에 따른 방향 전환
                    cell = grid[curr_r][curr_c]
                    if cell == 'L':
                        curr_d = (curr_d - 1) % 4
                    elif cell == 'R':
                        curr_d = (curr_d + 1) % 4
                    # 'S'일 경우 curr_d 유지
                
                answer.append(count)
                
    answer.sort()
    return answer

if __name__ == "__main__":
    grid = ["SL","LR"]
    ans = solution(grid)
    print(f"solution(grid): {ans} is_correct: {ans == [16]}")  # Output: [16]

    grid = ["S"]
    ans = solution(grid)
    print(f"solution(grid): {ans} is_correct: {ans == [1, 1, 1, 1]}")  # Output: [1, 1, 1, 1]

    grid = ["R", "R"]
    ans = solution(grid)
    print(f"solution(grid): {ans} is_correct: {ans == [4, 4]}")  # Output: [4, 4]
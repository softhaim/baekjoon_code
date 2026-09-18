'''
문제 설명
정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 1,000 이하입니다.

입출력 예
n	result
4	[1,2,9,3,10,8,4,5,6,7]
5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
'''
def solution(n):
    dp = [[0] * n for _ in range(n)]
    x, y, num = -1, 0, 1
    
    # 방향: 아래(x+1), 오른쪽(y+1), 대각선 위(x-1, y-1)
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    for i in range(n):
        for _ in range(n - i):
            angle = i % 3  # 0: 아래, 1: 오른쪽, 2: 대각선 위
            x += dx[angle]
            y += dy[angle]
            dp[x][y] = num
            num += 1

    # 0이 아닌 값만 1차원 리스트로 flattening
    return [val for row in dp for val in row if val != 0]

if __name__ == "__main__":
    io = [
        (4, [1,2,9,3,10,8,4,5,6,7]),
        (5, [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]),
        (6, [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]),
    ]
    ans = [solution(i[0]) for i in io]
    for i in io:
        print(f"Input: {i[0]}, Expected: {i[1]}, Got: {ans[io.index(i)]} is {'Correct' if ans[io.index(i)] == i[1] else 'Incorrect'}")
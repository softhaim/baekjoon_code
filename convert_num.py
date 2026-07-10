'''
문제 설명
자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.

x에 n을 더합니다
x에 2를 곱합니다.
x에 3을 곱합니다.
자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.

제한사항
1 ≤ x ≤ y ≤ 1,000,000
1 ≤ n < y

입출력 예
x	y	n	result
10	40	5	2
10	40	30	1
2	5	4	-1

bfs를 이용하여 x에서 y까지의 최소 연산 횟수를 구하는 문제였음.
'''

from collections import deque

def bfs(x, y, n):
    que = deque()
    que.append(x)
    visited = [-1]*(y+1)
    visited[x] = 0
    
    while que:
        now = que.popleft()
        if now == y:
            return visited[now]
        for dx in ((now+n), (now*2), (now*3)):
            if dx>y or visited[dx] != -1:
                continue
            que.append(dx)
            visited[dx] = visited[now] + 1
    return -1

def solution(x, y, n):
    return bfs(x,y,n)

if __name__ == "__main__":
    x = 10
    y = 40
    n = 5
    print(f"solution({x}, {y}, {n}) = {solution(x,y,n)} Gold ANS: 2") # 2

    x = 10
    y = 40
    n = 30
    print(f"solution({x}, {y}, {n}) = {solution(x,y,n)} Gold ANS: 1") # 1

    x = 2
    y = 5
    n = 4
    print(f"solution({x}, {y}, {n}) = {solution(x,y,n)} Gold ANS: -1") # -1
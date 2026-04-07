import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    K = int(input())
    que = deque()
    for _ in range(K):
        input_num = int(input())
        if input_num != 0:
            que.append(input_num)
        else:
            que.pop()
    result = 0
    while que:
        result += que.popleft()
    print(result)
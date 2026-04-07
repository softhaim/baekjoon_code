import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    input_num = list(map(int, input().split()))
    que = deque()
    for idx, val in enumerate(input_num, 1):
        que.append((idx, val))

    result = []
    idx, val = que.popleft() # 첫번째꺼 무조건 뺌
    result.append(idx)

    while que:
        if val > 0: # 양수인 경우
            for i in range(val-1):
                que.append(que.popleft())
            idx, val = que.popleft()
            result.append(idx)
        else:
            for i in range(abs(val)):
                que.appendleft(que.pop())
            idx, val = que.popleft()
            result.append(idx)
    print(*result)
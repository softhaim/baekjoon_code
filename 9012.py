import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())

    for t in range(T):
        input_str = list(input().strip())
        que = deque()
        cnt = 0
        for i in range(len(input_str)):
            if input_str[i] == "(":
                que.append("(")
                cnt += 1
            elif len(que) != 0:
                que.pop()
                cnt -= 1
            else:
                cnt -= 1
        if len(que) != 0 or cnt < 0:
            print("NO")
        else:
            print("YES")
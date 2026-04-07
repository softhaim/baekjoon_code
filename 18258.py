'''
명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    que = deque()
    for _ in range(N):
        input_op = list(input().split())
        op = input_op[0]
        if op == "push":
            que.append(input_op[1])
        elif op == "pop":
            if len(que) != 0: print(que.popleft())
            else: print(-1)
        elif op == "size":
            print(len(que))
        elif op == "empty":
            if len(que) == 0: print(1)
            else: print(0)
        elif op == "front":
            if len(que) != 0: print(que[0])
            else: print(-1)
        elif op == "back":
            if len(que) != 0: print(que[-1])
            else: print(-1)
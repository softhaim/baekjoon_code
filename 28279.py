'''
명령은 총 여덟 가지이다.

1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
5: 덱에 들어있는 정수의 개수를 출력한다.
6: 덱이 비어있으면 1, 아니면 0을 출력한다.
7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
'''

import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    que = deque()
    for i in range(N):
        op_input = list(map(int, input().split()))
        op = op_input[0]

        if op == 1:
            que.appendleft(op_input[1])
        elif op == 2:
            que.append(op_input[1])
        elif op == 3:
            if len(que) != 0: print(que.popleft())
            else: print(-1)
        elif op == 4:
            if len(que) != 0: print(que.pop())
            else: print(-1)
        elif op == 5:
            print(len(que))
        elif op == 6:
            if len(que) == 0: print(1)
            else: print(0)
        elif op == 7:
            if len(que) != 0: print(que[0])
            else: print(-1)
        elif op == 8:
            if len(que) != 0: print(que[-1])
            else: print(-1)
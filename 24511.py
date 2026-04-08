'''
스택이면 어차피 그대로 넘어가고 큐여야만 값이 바뀔것임. 
-> 이 말은 값을 삽입하면, 마지막 순서의 큐에 담긴 원소가 pop 되는것이고 거기에 삽입되는 것은 그 이전 순서의 큐의 값.
-> 큐에서의 원소 값만 deque 로 만들어두고, 값을 새로 넣으려 하는것을 appendleft 하고 해당 deque 에서 pop하여 출력하면 된다는 것임. 

초기 상태 : 
$[1, 2, 3, 4]$
첫 번째 원소 삽입 : 
$[2, 2, 3, 1]$
두 번째 원소 삽입 : 
$[4, 2, 3, 2]$
세 번째 원소 삽입 : 
$[7, 2, 3, 4]$

잘 보면 2,3 은 그대로고, 큐에서만 값이 바뀌고, 여기서 빠지는 순서는 4,1,2 로 큐에서의 값들의 뒤에서 부터의 순서대로이다. 이후는 삽입된 순서. 4-1-2-4-7 순서로 뒷자리가 바뀌는 규칙을 보고 결과를 저장하고 출력하면 된다.
'''

import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    is_stack = list(map(int, input().split()))
    B = list(map(int, input().split()))
    M = int(input())
    C = list(map(int, input().split()))
    q = deque()

    for i in range(N):
        if is_stack[i] == 0: 
            q.append(B[i])
    result = []
    for x in C:
        q.appendleft(x)
        result.append(q.pop())

    print(*result)
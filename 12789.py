'''
사람들은 현재 1열로 줄을 서있고, 맨 앞의 사람만 이동이 가능하다. 인규는 번호표 순서대로만 통과할 수 있는 라인을 만들어 두었다. 
이 라인과 대기열의 맨 앞 사람 사이에는 한 사람씩 1열이 들어갈 수 있는 공간이 있다. 
현재 대기열의 사람들은 이 공간으로 올 수 있지만 반대는 불가능하다. 승환이를 도와 프로그램을 완성하라.
'''

import sys
from collections import deque

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    original = list(map(int, input().split()))
    que = deque()
    find_num = 1
    for val in original:
        if val != find_num:
            que.append(val)
        else:
            find_num += 1
        while que and que[-1] == find_num:
            val = que.pop()
            find_num += 1

    if find_num-1 == N:
        print("Nice")
    else:
        print("Sad")
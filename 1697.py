'''
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
'''

'''
우선 드는 생각은 그냥 단순 정수 입력되고 이에 대해서 위치를 찾는거니까 다 0 해두고 그렇게 해서 수빈이 위치에서 출발해서 순간이동 하든 걷든 해서 bfs해서 큐에 넣어두고
각 점프 직전의 값을 기반으로 + 1 씩해서 기록 해둠 그렇게 0 인데 탐색하고 아닌데는 숫자이니 탐색안함.
'''

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

map_arr = [0]*(max(N,K)+2) # +2의 이유는 저 K 값에서 -1 해서 찾아올 수 있는 점과, 1~max까지라서 1-index라 +1 해줘야해서 총 +2 해준것. 이렇게 해도 통과 됨.

def bfs(a):
    queue = deque()
    queue.append(a)

    while queue:
        nx = queue.popleft()
        if nx == K: # 처음 출발위치에 대해서 이전 코드에서 안했는데 이거 넣어봄. 출발 하자마자 정답인 경우도 있을 수 있으니.
            return
        for x in (nx-1, nx+1, nx*2):
            if x < 0 or x >= len(map_arr):
                continue
            elif x == K: # 찾았으니까 더이상 할 필요 없으니 값 저장하고 끝
                map_arr[x] = map_arr[nx] + 1
                return
            elif map_arr[x] == 0:
                queue.append(x)
                map_arr[x] = map_arr[nx] + 1

    return

bfs(N)
print(map_arr[K])
'''
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성

bfs로 딱봐도 푸는건데, 예전에 비슷한 문제가 있었던거 같음. 그것도 순간이동이였는데 흠.
경로 출력이 다른듯. 그땐 경로 출력은 없었음.
'''

import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append(N)
    dp[N] = 0
    len_dp = len(dp)

    while que:
        nx = que.popleft()
        if nx == K:
            return dp[nx]
        for i in (nx-1, nx+1, nx*2):
            if 0<=i<=len_dp-1 and dp[i] == -1:
                prev[i] = nx
                dp[i] = dp[nx]+1
                que.append(i)

if __name__ == "__main__":
    N, K = map(int, input().split())

    max_val = 10**5

    dp = [-1]*(max_val+2) # 최대값보다 한칸 더 앞 간뒤 뒤로 빠꾸가 가능해서. + 2 한거. 0부터라는 점 주의.
    prev = [0]*(max_val+2)

    print(bfs())
    
    i = K
    result_prev = [K]
    while i != N:
        result_prev.append(prev[i])
        i = prev[i]
    result_prev.reverse()
    print(*result_prev)
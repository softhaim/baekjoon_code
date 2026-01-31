'''
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 
1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
'''

'''
3
26 40 83
49 60 57
13 89 99

출력 96
26 60 13 이니까

모든 위치에서 앞집과 다른 색으로 최소비용을 계산해줌으로써 색이 겹치지 않게 집을 칠하는 비용의 최솟값을 도출할 수 있다.

이를 점화식으로 표현하면 다음과 같다.
dp[i]["빨강"] = min(dp[i-1]["초록"], dp[i-1]["파랑"]) + RGB[i]["빨강"]
dp[i]["초록"] = min(dp[i-1]["빨강"], dp[i-1]["파랑"]) + RGB[i]["초록"]
dp[i]["파랑"] = min(dp[i-1]["빨강"], dp[i-1]["초록"]) + RGB[i]["파랑"]
'''

import sys

input = sys.stdin.readline

N = int(input())
dp = [([0]*3) for i in range(N)] # 3 x n 배열 만듦

color_cost = [list(map(int, input().strip().split())) for i in range(N)]

dp[0] = color_cost[0]

for i in range(1,N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + color_cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + color_cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + color_cost[i][2]

print(min(dp[-1]))
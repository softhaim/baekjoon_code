'''
dp로 푸는 문제이고, dfs로 처음에는 경우의 수 들어가면서 풀어야 하나 했지만, 그러면 터질것임.
코인이 1인 경우는 목표 값까지 해서 1,2,3,.. 에서 각 dp 에 경우의 수 1씩 추가.
2인 경우는 목표값까지 오는 경로의 경우의 수에서 2원 추가이니까, dp[i-2] 의 경우의 수와 같을 것임(여기서 단순 2원 추가한 것이니까 경우의 수는 저 i-2의 경우의 수와 같음).
dp[i] = dp[i-coin]해서 풀자. 
'''

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

dp = [0]*(k+1)
dp[0] = 1
for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

print(dp[k])

'''
맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.
'''
'''
5

    7
   3 8
  8 1 0
 2 7 4 4
4 5 2 6 5

출력 : 30
이는 7 3 8 7 5 = 30 이다.

여기서 점화식은
dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 현재값
0 및 끝의 경우는 dp[i-1][j] + 현재값, dp[i-1][j-1] + 현재값 일것이다. 

'''
import sys

input = sys.stdin.readline

N = int(input())

tree_arr = [list(map(int, input().strip().split())) for i in range(N)]

dp = [([0]*N) for i in range(N)] # n x n 만듦

dp[0] = tree_arr[0]

for i in range(1,N):
    for j in range(len(tree_arr[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tree_arr[i][j]
        elif j == len(tree_arr[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + tree_arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tree_arr[i][j]

print(max(dp[-1]))
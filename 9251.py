'''
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

예시 입력
ACAYKP
CAPCAK

예시 출력
4

알고리즘
dp[i][j] = dp[i-1][j-1] + 1 if str1[i] == str2[j]
          else max(dp[i-1][j], dp[i][j-1])

dp[i][j] = 두 문자열의 i번째 문자와 j번째 문자가 같을 때, 두 문자열의 i-1번째 문자와 j-1번째 문자의 LCS 길이 + 1
          else 두 문자열의 i-1번째 문자와 j번째 문자의 LCS 길이와 두 문자열의 i번째 문자와 j-1번째 문자의 LCS 길이 중 큰 값
'''

import sys

input = sys.stdin.readline

frist_str = input().strip()
second_str = input().strip()

dp = [[0]* (len(second_str)+1) for _ in range(len(frist_str)+1)] # 2차원 각각 길이에 대한 dp 배열 초기화

for i in range(1, len(frist_str)+1):
    for j in range(1, len(second_str)+1):

        if frist_str[i-1] == second_str[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(frist_str)][len(second_str)])

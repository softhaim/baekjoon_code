'''
문자 하나씩 비교해서
문자가 같으면
그 문자를 마지막에 붙여서 길이가 1 늘어남.

문자가 다르면
둘 다 동시에 쓸 수는 없으니

A[i-1]를 버리거나

B[j-1]를 버리는

두 경우 중 더 큰 걸 가져옴.

역추적해서 print하는 것도
문자가 같으면
A[i-1] == B[j-1]

이 문자는 LCS에 포함된 것이므로 저장하고

i -= 1
j -= 1

대각선 위로 이동

문자가 다르면

dp[i][j]가 어디서 왔는지 따라가야 함.

if dp[i-1][j] >= dp[i][j-1]:
    i -= 1
else:
    j -= 1

이렇게 이동.

즉,

위쪽 값이 더 크거나 같으면 위로

아니면 왼쪽으로
'''

import sys

input = sys.stdin.readline

def lcs_arr():
    # 길이 찾는 과정
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # 역추적
    i,j = n, m
    lcs = []

    while i>0 and j>0:
        if A[i-1] == B[j-1]:
            lcs.append(A[i-1])
            j -= 1
            i -= 1
        else: 
            if dp[i][j-1] > dp[i-1][j]: # 왼쪽 값이 더 크면 왼쪽 이동. 아니면 위로 위동.
                j -= 1
            else:
                i -= 1
    lcs.reverse()

    return lcs

if __name__ == "__main__":
    A = input().strip()
    B = input().strip()

    n = len(A)
    m = len(B)

    dp = [[0]*(m+1) for i in range(n+1)]

    lcs_result = lcs_arr()

    print(dp[n][m])
    print("".join(lcs_result))
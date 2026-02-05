'''
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만, 
{1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성


일반적인 dp 최장 수열 구하는 법은 
if arr[j] < arr[i]:
    dp[i] = max(dp[i], dp[j] + 1)

이를 거꾸로 하여 뒤에서 부터 구하면 역방향의 최장 수열로 감소하는 내림차순의 수열을 구할 수 있다.

for i in range(N, 0, -1):
    for j in range(i, 0, -1):
        if arr[j] < arr[i]
        dp[i] = max(dp[i], dp[j]+1) 

대략 이럴 것이다.

이렇게 구하고 나서 저 2개의 dp를 합치고 나서, 수열의 최대값 부분은 겹치는 원소로 들어가니까, 이를 제외하기 위해 -1 해준다.
for idx, val in enumerate(dp):
    dp[idx] = val -1

'''

import sys

input = sys.stdin.readline

N = int(input())

input_arr = [0]
input_arr = input_arr + list(map(int, input().split()))

dp_right = [0]*(N+1)
dp_left = [0]*(N+1)
dp_all = [0]*(N+1)

for i in range(1, N+1):
    for j in range(i):
        if input_arr[j] < input_arr[i]: 
            dp_right[i] = max(dp_right[i], dp_right[j]+1)

for i in range(1, N+1):
    for j in range(i):
        if input_arr[-j] < input_arr[-i]: 
            dp_left[-i] = max(dp_left[-i], dp_left[-j]+1)

for i in range(N+1):
    dp_all[i] = (dp_right[i] + dp_left[i] -1)

print(max(dp_all))
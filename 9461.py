'''
파도반 수열 p(n) 은 나선에 있는 정삼각형의 벼의 길이
p(1) = 1
p(2) = 1
p(3) = 1
p(4) = 2
p(5) = 2
p(6) = 3
p(7) = 4
p(8) = 5
p(9) = 7
p(10) = 9

N 이 주어졌을 대, p(n)을 구하는 프로그램을 작성하시오.

여기서 규칙은 P(n) = p(n-1) + p(n-5) 이다.
'''

import sys

input = sys.stdin.readline
T = int(input())

def print_pn(n, dp):
    if n <= 3 and n > 0:
        dp[n] = 1
    elif n == 4:
        dp[n] = 2
    elif n >= 5 and dp[n-1] != 0 and dp[n-5] != 0 :
        dp[n] = dp[n-1] + dp[n-5]
    elif not n < 0:
        dp[n] = print_pn(n-1, dp) + print_pn(n-5, dp)
    elif n < 0:
        return 0
    return dp[n]


for _ in range(T):
    N = int(input())
    dp = [0] * (N+1)
    
    print(print_pn(N, dp))

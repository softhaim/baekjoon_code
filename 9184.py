'''
입력
입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다. 
입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

출력
입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.
'''

'''
다음과 같은 재귀함수 w(a, b, c)가 있다. 근데 이건 너무 오래걸리니까 dp 를 이용해서 해결하자.

if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
'''

import sys
input = sys.stdin.readline

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)] # 3차원 배열 초기화

def w(a, b, c):
    if a <=0 or b <=0 or c <=0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        if dp[a][b][c-1] != 0 and dp[a][b-1][c-1] != 0 and dp[a][b-1][c] != 0:
            dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
        else:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        if dp[a-1][b][c] != 0 and dp[a-1][b-1][c] != 0 and dp[a-1][b][c-1] != 0 and dp[a-1][b-1][c-1] != 0:
            dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]
        else:
            dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
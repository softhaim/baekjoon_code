import sys
input = sys.stdin.readline

N, M = map(int, input().split())

map_arr = []
for i in range(N):
    map_arr.append(list(map(int, input().split())))  # int로 받기

# sum_dp[i][j] = (1,1) ~ (i,j)까지의 누적합 (1-indexed로 패딩)
sum_dp = [[0] * (N + 1) for _ in range(N + 1)]

# 누적합 채우기
for i in range(1, N + 1):
    for j in range(1, N + 1):
        '''
        여기서 윗 행에서는 j 까지 누적합과 j-1 누적합 빼면서 i,j 에서의 이로 인해 추가되는 열의 내용을 더함.
        그다음 행에 대한 내용으로 i부터 j-1까지 합한 값을 더하고 현재 값 더함.
        '''
        sum_dp[i][j] = (
            sum_dp[i - 1][j]
            + sum_dp[i][j - 1]
            - sum_dp[i - 1][j - 1]
            + map_arr[i - 1][j - 1]
        )

# 질의 처리
out = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    '''
    값을 구하기 위해서는 x2 y2 해당하는 사각형의 누적합에서, x1, y1에 해당하는 좌표 왼쪽과 위의 값을 지워야함.
    x1-1 과 y2가 될거고 왼쪽 뺄거는, x2 y1-1 이 위쪽 뺄거다. 
    여기서 공통적으로 x-1, y-1 부분은 2번 빼지니까 한번 더해준다. 
    '''
    find_ans = (
        sum_dp[x2][y2]
        - sum_dp[x1 - 1][y2]
        - sum_dp[x2][y1 - 1]
        + sum_dp[x1 - 1][y1 - 1]
    )
    out.append(str(find_ans))

print("\n".join(out))

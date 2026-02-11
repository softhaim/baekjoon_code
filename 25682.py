'''
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 
지민이는 이 보드를 잘라서 K×K 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 
변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 K×K 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
당연히 K×K 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''


'''
반대로 안칠해도 되는 최대 개수를 구할 것인지도 고려.

아니면 bw 가 하나의 세트로 보고 이것이 아닌 개수?   

0,1로 만들어진 행렬에서 1을 최소로 가지는 위치를 찾아낼 때 사용되는 것이 바로 누적합. 1은 바꿔야 하는 것
왼쪽 위가 하얀색, 검은색 2가지 경우의 수를 기반으로 누적합을 한 뒤, 이를 기반으로 찾음
4x4 에서 3 들어왔을 때의 가능한 위치를 구하면 최소 3,3 부터 x와 y가 저 3 이상의 값으로 다 선택해보면서 뭐가 작은지 찾음.
이째 선택으로 인해 구성되는 사각형은 i,j - (i-k,j) - (i,j-k) + i-k,j-k 를 해주면 될 것이다. 
당연히 누적합은 2차원 사각형의 누적합으로 저장해둬야할 것임.
'''

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

map_arr = []

for i in range(N):
    map_arr.append(list(input().strip()))

white_start_dp = [ [0] * (M+1) for i in range(N+1) ] # 처음이 b 인거 
black_start_dp = [ [0] * (M+1) for i in range(N+1) ] # 처음이 w 인거

# 여기서 부터 누적합을 구함
for i in range(1, N+1):
    for j in range(1, M+1):
        # 화이트 시작은 i 가 홀수일때, j가 홀수이고 짝수일때는 j도 짝수일때 화이트면 됨. 블랙은 반대로 짝수일 때.
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0): # 둘 다 짝수의 경우거나 둘 다 홀수인 경우
            if map_arr[i-1][j-1] == "B": # 둘다 짝/홀 경우에 시작한 색상과 동일 해야함. 
                black_start_dp[i][j] = black_start_dp[i-1][j] + black_start_dp[i][j-1] - black_start_dp[i-1][j-1] # B이니까 굳이 안바꿔도 됨.
                white_start_dp[i][j] = white_start_dp[i-1][j] + white_start_dp[i][j-1] - white_start_dp[i-1][j-1] + 1 # B이니까 변경해야하니 +1 해줌
            else: # w 인 경우
                black_start_dp[i][j] = black_start_dp[i-1][j] + black_start_dp[i][j-1] - black_start_dp[i-1][j-1] + 1# w 이니까 + 1 해줌
                white_start_dp[i][j] = white_start_dp[i-1][j] + white_start_dp[i][j-1] - white_start_dp[i-1][j-1] # w이니까 그냥
        else: # 이 경우는 둘 중 하나라도 다른 홀/짝 안맞는 경우 => 시작 색상과 다른 색임. 
            if map_arr[i-1][j-1] == "W":  
                black_start_dp[i][j] = black_start_dp[i-1][j] + black_start_dp[i][j-1] - black_start_dp[i-1][j-1] # 굳이 안바꿔도 됨.
                white_start_dp[i][j] = white_start_dp[i-1][j] + white_start_dp[i][j-1] - white_start_dp[i-1][j-1] + 1 # 변경해야하니 +1 해줌
            else: # B 인 경우
                black_start_dp[i][j] = black_start_dp[i-1][j] + black_start_dp[i][j-1] - black_start_dp[i-1][j-1] + 1# 변경 해야하니까 + 1 해줌
                white_start_dp[i][j] = white_start_dp[i-1][j] + white_start_dp[i][j-1] - white_start_dp[i-1][j-1] # 그냥


# 누적합은 다 구했으니까 이제 답을 구할 차례. 
min_ans = N*M
for i in range(K, N+1):
    for j in range(K, M+1):
        black_ans = black_start_dp[i][j] - black_start_dp[i-K][j] - black_start_dp[i][j-K] + black_start_dp[i-K][j-K]
        white_ans = white_start_dp[i][j] - white_start_dp[i-K][j] - white_start_dp[i][j-K] + white_start_dp[i-K][j-K]
        min_ans = min(min_ans, black_ans, white_ans)

print(min_ans)
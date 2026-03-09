'''
5 60
30 10 20 35 40
3 0 3 5 4

대충 이렇게 입력일때 3 0 3 꺼서 60 이상 메모리 확보하면서 가장낮은 비용으로 하는것임. 

냅색처럼 풀면 될거 같긴한데 최소의 비용을 찾고자 하는 것. 게다가 반대로 무게도 원래는 저 무게 안에서 넣는건데 다 채워서 넘칠때까지 넣음. 
냅색은 해당 무게일때 담을 수 있는 최대의 cost 를 dp 로 저장하는 것이기에
해당하는 비용이 기준일 때, 여기서는 최대로 얻을 수 있는 메모리의 값을 저장하도록 한다.
기존에는 마지막 무게가 최종 가방무게이고 이때 최대로 담는 값이 얼마인지 궁금하기에 dp[미지막][마지막] 했지만, 여기서는 비용이 최대 비용일때 최대 메모리가 궁금한게 아님.
M 메모리 이상을 담을 수 있을 때, 그때의 최소의 j값 (cost)이 궁금한것. 그러기에 이것을 저장하도록 따로 변수 두고 저장을 해둠. min 값으로. 

dp[i][j]는 i번째 앱까지 중 j코스트로 얻을 수 있는 최대의 byte

기본 냅색 알고리즘은 
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = wv_lst[i][0]
        value = wv_lst[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
이다. 
'''

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int,input().split())

    memory = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    sum_cost = sum(cost)

    dp = [[0]*(sum_cost+1) for i in range(N+1)]
    min_cost = float('inf')

    for i in range(1, N+1):
        # 입력때 앞에 0 idx 부터 넣어놔서 -1 idx 해준 것.
        memory_i = memory[i-1]
        cost_i = cost[i-1]

        for j in range(sum_cost+1): # 비용이 0 인거도 있어서 0 부터 시작.
            if j < cost_i: # 해당 cost 만큼 충분하지 않은 idx값
                dp[i][j] = dp[i-1][j] # 안담을거라서 위에서의 결과와 같음. 현재껄 안담았으니.
            else: # 담을 수 있음
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost_i] + memory_i) # 담는 것이 이전까지의 값과 비교해서 담는것이 좋으면 담음.
                if dp[i][j] >= M:
                    min_cost = min(min_cost, j)

    print(min_cost)
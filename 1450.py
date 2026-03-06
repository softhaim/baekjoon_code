'''
냅색 문제. 기본 냅색 알고리즘은 이럼. 
현재 가방에 담을 수 있는 무게)가 현재 물건의 무게 w보다 작을 때
현재 물건을 담을 수 없으므로, 이전 물건에서의 i에 해당하던 값(i-1)을 넣어준다.
j가 현재 물건의 무게 w와 같거나 클 때

현재 물건을 담을 수 있음
물건을 담았을 때와 담지 않았을 때의 가치를 비교해준 뒤, 더 큰 값을 할당해줌
현재 물건의 가치는 v

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = wv_lst[i][0]
        value = wv_lst[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
물건의 최대 가치는 dp[가방 크기][물건의 개수]로 구할 수 있다.

N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성.
근데 문제가 이거라서 위 알고리즘은 해당이 안되는듯함... 위는 가치를 구하는 알고리즘임.
컨닝좀 해보니, 분할해서 앞,뒤 절반 나누고 각각의 부분 집합의 합을 구해둚. 
앞 기준으로 해당 무게 넣었을때 뒤에서 전체 무게 - 앞무게 >= 뒤에서 넣을 수 있는무게 이므로 bisect_right(right, C - left_sum) 해서 나온 값이 경우의 수임.

'''

import sys
from bisect import bisect_right

input = sys.stdin.readline

def dfs(idx, sum_val, arr, result):
    if sum_val > C:
        return
    
    if idx == len(arr):
        result.append(sum_val)
        return
    
    dfs(idx+1, sum_val, arr, result) # 지금 원소를 안넣은 경우
    dfs(idx+1, sum_val + arr[idx], arr, result) # 지금 원소를 넣은 경우

N, C = map(int, input().split())

arr = list(map(int, input().split()))

left = arr[:N//2]
right = arr[N//2:]

left_sum = []
right_sum = []


dfs(0,0,left,left_sum)
dfs(0,0,right,right_sum)
right_sum.sort()

ans = 0

for s in left_sum:
    ans += bisect_right(right_sum, C-s) # 해당 인덱스 이전까지의 부분합의 경우의 수는 전부 가능하니 bisect_right 로 찾은 해당 인덱스 값을 넣음 
print(ans)
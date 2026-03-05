'''
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
슬라이딩 윈도우로 해서 하니씩 넣으면서 그 부분 수열 합이 목표되는지 확인
''' 

import sys

input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int,input().split()))

left = 0
right = N-1
min_len = float('inf')
sum_num = 0

for right in range(N):
    sum_num += arr[right]

    while sum_num >= S: # 합이 이상이 되는 것 중 이니 >= 씀 
        min_len = min(min_len, right - left + 1) # 우선 현재 min_len 기록 해둚
        sum_num -= arr[left] # 기록 해둔 뒤에 이제 왼쪽꺼 하나씩 뺌. 이래도 S보다 같거나 이상이면 min값 갱신하는거고 아니면 조건 벗어사서 right 넣어서 다시 보고.
        left += 1

print(min_len if min_len != float('inf') else 0)
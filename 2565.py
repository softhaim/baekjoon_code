'''
두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다.

합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다.

예를 들어, < 그림 1 >과 같이 전깃줄이 연결되어 있는 경우 A의 1번 위치와 B의 8번 위치를 잇는 전깃줄,

A의 3번 위치와 B의 9번 위치를 잇는 전깃줄, A의 4번 위치와 B의 1번 위치를 잇는 전깃줄을 없애면 남아있는 모든 전깃줄이 서로 교차하지 않게 된다.
'''

'''
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6

출력 3

1. 왼쪽 전봇대를 기준으로 정렬을 시켜준다.
2. 오른쪽 전봇대에서 "가장 긴 증가하는 부분 수열"을 구해준다.
3. 2번과정에서 구한 "가장 긴 증가하는 부분 수열"의 크기를 N에서 빼준다.

1 8 
2 2
3 9
4 1
6 4
7 6
9 7
10 10

으로 정렬 후에
[8,2,9,1,4,6,7] 에서 최장 수열 구하면, 1,4,6,7 이 될거다. N-최장 해주면 버리는 것 구할 수 있는것.
'''

import sys
from bisect import bisect_left 

input = sys.stdin.readline

N = int(input())

input_arr =[]

for i in range(N):
    input_arr.append(list(map(int, input().split())))

# 왼쪽 기준 정렬
input_arr.sort(key=lambda x : x[0])

def lts(arr):
    tails = []               # 길이별 "최소 꼬리값"을 저장하는 배열 (정렬 유지)
    L = [0] * len(arr)       # i에서 끝나는 LIS 길이를 저장
    
    for i, x in enumerate(arr):
        pos = bisect_left(tails, x[1])
        
        if pos == len(tails):
            tails.append(x[1])
        else:
            tails[pos] = x[1]
        
        L[pos] = pos + 1
    return L

lts_arr = lts(input_arr)

print(N-max(lts_arr))
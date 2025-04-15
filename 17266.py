#17266

'''
입력
첫 번째 줄에 굴다리의 길이 N 이 주어진다. (1 ≤ N ≤ 100,000)

두 번째 줄에 가로등의 개수 M 이 주어진다. (1 ≤ M ≤ N)

다음 줄에 M 개의 설치할 수 있는 가로등의 위치 x 가 주어진다. (0 ≤ x ≤ N)

가로등의 위치 x는 오름차순으로 입력받으며 가로등의 위치는 중복되지 않으며, 정수이다.

출력
굴다리의 길이 N을 모두 비추기 위한 가로등의 최소 높이를 출력한다.
'''

'''
5 -> 굴다리 길이
2 -> 가로등 개수
2 4 -> 가로등 위치
들어왔을 때, 
가로등의 높이가 H라면 왼쪽으로 H, 오른쪽으로 H만큼 주위를 비춘다.
가로등의 높이가 1일 경우 0~1사이의 길이 어둡기 때문에 상빈이는 지나가지 못한다.

아래 그림처럼 높이가 2일 경우 0~5의 모든 길이 밝기 때문에 상빈이는 지나갈 수 있다.
'''
'''
3칸 차이일때 => 1나올것

2 -] - [- 5 

이렇게 되니까 + 1 해주는게 맞았음.
'''

import sys
input = sys.stdin.readline

N = int(input())  # 굴다리의 길이
M = int(input())  # 가로등의 개수
x = list(map(int, input().split()))  # 가로등 위치

# 최소 높이 계산
max_gap = 0

# 두 가로등 사이의 최대 간격 계산
for i in range(1, M):
    max_gap = max(max_gap, (x[i] - x[i-1]))

# 첫 가로등 이전 구간과 마지막 가로등 이후 구간 계산
max_start_gap = x[0]  # 첫 가로등까지의 거리
max_end_gap = N - x[-1]  # 마지막 가로등부터 끝까지의 거리

# 필요한 최소 높이는 위의 값들 중 최대값
min_height = max(max_start_gap, max_end_gap, (max_gap + 1) // 2)

print(min_height)
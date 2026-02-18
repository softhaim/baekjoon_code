'''
세계적인 도둑 상덕이는 보석점을 털기로 결심했다.

상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 
상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.

상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

'''

import sys, heapq
from unittest import result

input = sys.stdin.readline

N, K = map(int,input().split())

gems = []
# [M_i, V_i] 로 해서 넣음.
for i in range(N):
    gems.append(list(map(int,input().split())))
gems.sort()

bags = []
for j in range(K):
    bags.append(int(input()))
bags.sort()

'''
보석의 무게, 가격 리스트와 가방의 무게 리스트를 오름차순으로 정렬하고, 각 가방별로 훔칠 수 있는 보석을 최대힙을 통해 탐색하는게 핵심
'''
tmp = []
result = 0

'''
여기서 오름차순으로 정렬된 가방을 기준으로 작은 가방부터 담을 수 있는 최대 값을 tmp 에 최대힙으로 저장
그렇게 담을 수 있는 값 중 최대 값만 pop 해서 result에 저장.
이후 다음 가방은 오름차순이라 더 클 것이고, 이전에 담은 남은 값들과 추가로 현재 가방에 담을 수 있는 한계만큼의 값을 맥스 힙에 다시 넣고, 이 값중 다시 큰거 담으면 됨.
'''
for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(tmp, -gems[0][1])
        heapq.heappop(gems)
    if tmp:
        result -= heapq.heappop(tmp)
        
print(result)
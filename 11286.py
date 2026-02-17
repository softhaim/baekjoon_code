'''
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
'''

import heapq
import sys

input = sys.stdin.readline

abs_heap = []

N = int(input())

for i in range(N):
    input_num = int(input())

    if input_num != 0: 
        heapq.heappush(abs_heap, (abs(input_num),input_num)) # 여기서 핵심은 (abs(x), x)로 절댓값과 같이 넣음. 이러면 절댓값 우선 넣고 같으면 실제 원소 작은거로 함. 
    elif input_num == 0:
        try:
            pop_num = heapq.heappop(abs_heap)
            print(pop_num[1])
        except:
            print(0)
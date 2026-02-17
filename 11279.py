'''
널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다
'''

import sys
import heapq

input = sys.stdin.readline

N = int(input())

max_heap = []


for i in range(N):
    input_num = int(input())
    if input_num != 0:
        heapq.heappush(max_heap, -input_num) # 여기서 heapq 는 기본이 min heap 임. 그래서 max heap을 하려면 부호를 반대로 뒤집어서 넣어야 됨. 
    elif input_num == 0 and len(max_heap) !=0:
        print(-(heapq.heappop(max_heap))) # 기본이 min heap 이라서 부호 반대로 넣었으니까 출력할때는 부호 다시 - 붙여서 출력해야 최대 힙임. 
    else: 
        print(0)
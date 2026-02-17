'''
이전에는 min 힘으로 그냥 최솟값보다 큰 원소 들어오면 넣어주고 하는 식으로 풀었었음.

            if arr[0] < j: # 현재 최소값보다 크면 넣어줌
                heapq.heappop(arr)
                heapq.heappush(arr, j)

이렇게 했었음. 근데 보니까 max heap 으로 구성해서 그냥 풀고 5번째 원소 값 뽑는식으로는 틀리나 싶어서 한번 해봄.

=> max heap 하니까 메모리 초과가 뜸. 위처럼 해야하나 봄;
min heap 으로 결국 푸는 것이 이 문제의 정답으로 가는 핵심. top 원소를 비교하면서 배열을 N 크기로 두면서 작은값은 계속 빼면서 큰값만 더해줌.
그렇게 N개의 큰 값만 남기는 것. 
여기서 기존에는 pop 하고 push 했지만 이번에는 heapreplace 를 써보자. pop 하면서 push 하는 것이다. 
'''

import sys , heapq

input = sys.stdin.readline

heap = []

N = int(input())

for i in range(N):
    input_num = list(map(int, input().split()))

    for j in input_num:
        if len(heap) < N:
            heapq.heappush(heap, j)
        else:
            if j > heap[0]: # 최솟값보다 j 가 크다면 
                heapq.heapreplace(heap, j) # 힙에서 최솟값(루트)을 꺼내면서(pop) 동시에 새 값을 넣는(push)

print(heap[0])
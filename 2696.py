'''
어떤 수열을 읽고, 홀수번째 수를 읽을 때 마다, 지금까지 입력받은 값의 중앙값을 출력하는 프로그램을 작성하시오.

예를 들어, 수열이 1, 5, 4, 3, 2 이면, 홀수번째 수는 1번째 수, 3번째 수, 5번째 수이고, 1번째 수를 읽었을 때 중앙값은 1, 3번째 수를 읽었을 때는 4, 5번째 수를 읽었을 때는 3이다.
'''


'''
입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스의 첫째 줄에는 수열의 크기 M(1 ≤ M ≤ 9999, M은 홀수)이 주어지고, 
그 다음 줄부터 이 수열의 원소가 차례대로 주어진다. 원소는 한 줄에 10개씩 나누어져있고, 32비트 부호있는 정수이다.

출력
각 테스트 케이스에 대해 첫째 줄에 출력하는 중앙값의 개수를 출력하고, 둘째 줄에는 홀수 번째 수를 읽을 때 마다 구한 중앙값을 차례대로 공백으로 구분하여 출력한다. 이때, 한 줄에 10개씩 출력해야 한다.

'''
import sys, heapq

input = sys.stdin.readline

T = int(input())

'''
중앙값 문제는 보통 두 힙(최대힙/최소힙)으로 균형 유지해야 온라인으로 O(log n)에 됨
'''
for i in range(T):
    M = int(input())
    min_heap = []
    max_heap = []
    medians = []

    count = 0
    while count < M:
        input_num = list(map(int, input().split()))
        for j, val in enumerate(input_num):
            if count >= M:
                break
            count += 1

            # push
            if not max_heap or val <= -max_heap[0]:
                heapq.heappush(max_heap, -val)
            else:
                heapq.heappush(min_heap, val)
            
            # rebalance
            if len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, -(heapq.heappop(min_heap)))
            elif len(max_heap) > len(min_heap) + 1: # 처음에 한개 max힙에 먼저 넣어놨으니 +1 해서 비교
                heapq.heappush(min_heap, -(heapq.heappop(max_heap)))

            # 홀수 번째 기록
            if count % 2 == 1 :
                medians.append(-max_heap[0])

    print(len(medians))
    for i, val in enumerate(medians,1):
        print(val, end=" ")
        if i % 10 == 0: # 10줄마다 개행
            print() 
    if len(medians) % 10 != 0: # 10개 딱 끊겼으면 위에서 개행 됐을텐데 아니라면 개행 안되었을 테니 해줌
        print()
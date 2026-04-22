'''
문제 설명
이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

명령어	수신 탑(높이)
I 숫자	큐에 주어진 숫자를 삽입합니다.
D 1	큐에서 최댓값을 삭제합니다.
D -1	큐에서 최솟값을 삭제합니다.
이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

제한사항
operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
operations의 원소는 큐가 수행할 연산을 나타냅니다.
원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.
입출력 예
operations	return
["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	[0,0]
["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	[333, -45]
입출력 예 설명
입출력 예 #1

16과 -5643을 삽입합니다.
최솟값을 삭제합니다. -5643이 삭제되고 16이 남아있습니다.
최댓값을 삭제합니다. 16이 삭제되고 이중 우선순위 큐는 비어있습니다.
우선순위 큐가 비어있으므로 최댓값 삭제 연산이 무시됩니다.
123을 삽입합니다.
최솟값을 삭제합니다. 123이 삭제되고 이중 우선순위 큐는 비어있습니다.
따라서 [0, 0]을 반환합니다.

입출력 예 #2

-45와 653을 삽입후 최댓값(653)을 삭제합니다. -45가 남아있습니다.
-642, 45, 97을 삽입 후 최댓값(97), 최솟값(-642)을 삭제합니다. -45와 45가 남아있습니다.
333을 삽입합니다.
이중 우선순위 큐에 -45, 45, 333이 남아있으므로, [333, -45]를 반환합니다.
'''

import heapq, sys
input = sys.stdin.readline

def max_sync(max_heap, delete):
    while max_heap and delete.get(-max_heap[0], 0) > 0: # # 안비었고, 해당 최댓값이 삭제한 값이면 -> 삭제해버림 (동기화 작업)
        delete[-heapq.heappop(max_heap)] -= 1
    
def min_sync(min_heap, delete):
    while min_heap and delete.get(min_heap[0], 0) > 0: # 안비었고, 해당 최솟값이 삭제한 값이면 -> 삭제해버림 (동기화 작업)
        delete[heapq.heappop(min_heap)] -= 1

def synchronization(min_heap, max_heap, delete, del_val):
    if del_val == 1:
        max_sync(max_heap, delete)
        min_sync(min_heap, delete)
    else:
        min_sync(min_heap, delete)
        max_sync(max_heap, delete)

def solution(operations):
    min_heap = []
    max_heap = []
    delete = {}
    
    for cxt in operations:
        op, val = cxt.split()
        val = int(val)

        if op == "I":
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
        elif val == 1:
            if max_heap: # 삭제 했던거 아니면 -> 최댓값
                max_val = -heapq.heappop(max_heap)
                delete[max_val] = delete.get(max_val, 0) + 1
            synchronization(min_heap, max_heap, delete, val)
        elif val == -1: # 최솟값 삭제
            if min_heap: # 안비었다면 최소값 삭제
                min_val = heapq.heappop(min_heap)
                delete[min_val] = delete.get(min_val, 0) + 1
            synchronization(min_heap, max_heap, delete, val)

    # print(f"min_heap:{min_heap}")
    # print(f"max_heap:{max_heap}")
    # print(f"delete:{delete}")
        
    if not min_heap or not max_heap: 
        return [0, 0]
    
    return [-max_heap[0], min_heap[0]]

if __name__ == "__main__":
    print(f'{solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])}, gold ANS: [0, 0]')
    print(f'{solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])}, gold ANS: [333, -45]')
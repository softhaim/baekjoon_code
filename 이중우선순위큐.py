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

처음에 dic으로 풀면서 삭제해야하는것을 +1 하면서 했는데 이 경우, 같은 원소만 들어왔을때 1개만 지워야 하는데 
'''
import heapq

# def solution(operations):
#     min_heap = []
#     max_heap = []
#     visited = [False] * len(operations) # 들어온 명령어 순서대로 매겨놓고 해당 명령어내용 지웠는지 판단하는데 사용하는 dp 라 생각
    
#     for idx, cxt in enumerate(operations):
#         op, val = cxt.split()
#         val = int(val)

#         if op == "I":
#             heapq.heappush(min_heap, (val, idx))
#             heapq.heappush(max_heap, (-val, idx))
#         elif val == 1:
#             while max_heap and visited[max_heap[0][1]]: # 힙이 안비었고, 삭제했던거면
#                 heapq.heappop(max_heap) # 해당 값은 삭제
#             if max_heap: # 삭제 했던거 아니면 -> 최댓값
#                 _, i = heapq.heappop(max_heap)
#                 visited[i] = True
#         elif val == -1: # 최솟값 삭제
#             while min_heap and visited[min_heap[0][1]]: 
#                 heapq.heappop(min_heap)
#             if min_heap:
#                 _, i = heapq.heappop(min_heap)
#                 visited[i] = True
            
#     # 최솟값 및 최대값이 현재 삭제 해야 하는 값인데 안한 경우는 삭제
#     while min_heap and visited[min_heap[0][1]]:
#         heapq.heappop(min_heap)
#     while max_heap and visited[max_heap[0][1]]:
#         heapq.heappop(max_heap)
        
#     if not min_heap or not max_heap: 
#         return [0, 0]
    
#     return [-max_heap[0][0], min_heap[0][0]]

# 위 처럼 해야 안전하긴 하지만, 삭제 연산이 많을 수록 낭비됨. 딕셔너리로 하려면 아래처럼 들어간것을 세고, 그렇게 0되면 다 없애야 하는거니까 싹다 삭제하는식으로 동기화 하면 정답.
def min_sync(min_heap, count):
    while min_heap and count.get(min_heap[0], 0) == 0: # 0 인 경우에는 아예 이 값이 없어야 하니까 계속 버려야함. 아니면 하나라도 이 값이 있어야 하는거라서 안버려도 됨.
        heapq.heappop(min_heap)

def max_sync(max_heap, count):
    while max_heap and count.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)

def solution(operations):
    min_heap = []
    max_heap = []
    count = {}

    for cxt in operations:
        op, val = cxt.split()
        val = int(val)

        if op == "I":
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
            count[val] = count.get(val, 0) + 1

        elif val == 1:
            max_sync(max_heap, count)
            if max_heap:
                x = -heapq.heappop(max_heap)
                count[x] -= 1

        elif val == -1:
            min_sync(min_heap, count)
            if min_heap:
                x = heapq.heappop(min_heap)
                count[x] -= 1

    min_sync(min_heap, count)
    max_sync(max_heap, count)

    if not min_heap or not max_heap:
        return [0, 0]

    return [-max_heap[0], min_heap[0]]

if __name__ == "__main__":
    print(f'{solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])}, gold ANS: [0, 0]')
    print(f'{solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])}, gold ANS: [333, -45]')
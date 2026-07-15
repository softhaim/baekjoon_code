'''
우선순위 큐 사용

일단 내 병사 써서 일단 막는다고 가정해서 하고, maxheap에 저장

n<0 되는 순간 오면, maxheap에서 가장 적 많았던거 제외해서 병사 돌려받고, k-= 1함.
이렇게 n<0 and k == 0 이면, 이전까지만 진행 가능이였던거니까, 이전 라운드 반환하고 종료
'''
import heapq

def solution(n, k, enemy):
    max_heap = []
    
    for idx, val in enumerate(enemy, 1):
        n -= val
        heapq.heappush(max_heap, -val)
        while n<0:
            if k == 0:
                return idx-1
            n += -heapq.heappop(max_heap)
            k -= 1
            
    return len(enemy)
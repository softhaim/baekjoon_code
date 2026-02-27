'''
N개의 문제는 모두 풀어야 한다.
먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
가능하면 쉬운 문제부터 풀어야 한다.
'''

'''
입력으로 주어진 선행 관계만 그래프에 저장

각 노드의 진입차수(indegree) 계산

진입차수 0인 문제들을 최소 힙(min-heap) 에 넣음

힙에서 가장 작은 번호를 꺼내 정답에 추가

그 문제와 연결된 다음 문제들의 진입차수를 1씩 감소

새로 진입차수 0이 된 문제를 힙에 넣음

반복
'''

import sys, heapq


input = sys.stdin.readline

def main():
    N, M = map(int,input().split())
    graph = [[]*(N+1) for _ in range(N+1)]
    indegree = [0]*(N+1)

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        indegree[B] += 1
    # 핵심은 힙으로 구성해서 indegree가 0인거 우선 넣어두고, 그 다음에 진행하면서 result에 추가한 원소로 인해 제약이 해제된다면 그것을 넣을 텐데, 이것이 힙으로 인해 작은것부터(쉬운것부터 출력하게)정렬되어서 나옴. 이렇게 쉬운거부터 하도록 하는것.
    heap = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)

    result = []

    while heap:
        now = heapq.heappop(heap)
        result.append(now)

        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(heap, nxt)

    for val in result:
        print(val, end=" ")

if __name__ == "__main__":
    main()
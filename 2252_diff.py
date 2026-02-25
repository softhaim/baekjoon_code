'''
진입차수 = 나보다 먼저 와야 하는 사람 수

예제에서:

1로 들어오는 간선 없음 → indegree[1] = 0

2로 들어오는 간선 없음 → indegree[2] = 0

3으로는 1, 2가 들어옴 → indegree[3] = 2

즉:

indegree가 0인 학생은 지금 바로 줄 앞쪽에 세워도 되는 학생

누가 먼저 와야 한다는 조건이 아직 안 남아있기 때문

기존에는 그래프에 연결된 값을 저장했었는데 이번에는 false graph 로 해볼까 싶기도 함. (그냥 다른 풀이 느낌으로 3665 풀이처럼 해보려고)
인접 행렬이라 O(N²) 시간 / O(N²) 메모리

기존은 인접 리스트라 O(N+M) 시간 / O(N+M) 메모리

gpt 피셜 동작은 같다 함. 다만, 메모리 초과는 뜸. 
'''

import sys 
from collections import deque

input = sys.stdin.readline

def main():

    N, M = map(int, input().split())

    graph = [[False]*(N+1) for i in range(N+1)]
    indegree = [0]*(N+1)

    for i in range(M):
        A, B = map(int,input().split())
        graph[A][B] = True
        indegree[B] += 1

    queue = deque()

    for i in range(1,N+1):
        if indegree[i] == 0: # 바로 출력해도 되는 경우.
            queue.append(i)

    result = []
    '''
    위에서 바로 세워도 되는 경우는 다 넣었으니까 이것부터 출력을 하고 그렇게 해서 연결된 indegree 값을 -1 해줌
    '''
    while queue:
        val = queue.popleft()
        result.append(val)
        for i in range(1,N+1):
            if graph[val][i]:
                graph[val][i] = False # 이제 해당 위치에서의 제약은 햇으니까. 
                indegree[i] -= 1
                if indegree[i] == 0: # 다 조건이 해제되었으니까 값을 넣어줌
                    queue.append(i)

    for val in result:
        print(val, end=" ")

if __name__ == "__main__":
    main()
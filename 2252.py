'''
진입차수 = 나보다 먼저 와야 하는 사람 수

예제에서:

1로 들어오는 간선 없음 → indegree[1] = 0

2로 들어오는 간선 없음 → indegree[2] = 0

3으로는 1, 2가 들어옴 → indegree[3] = 2

즉:

indegree가 0인 학생은 지금 바로 줄 앞쪽에 세워도 되는 학생

누가 먼저 와야 한다는 조건이 아직 안 남아있기 때문
'''

import sys 
from collections import deque

input = sys.stdin.readline

def main():

    N, M = map(int, input().split())

    graph = [[] for i in range(N+1)]
    indegree = [0]*(N+1)

    for i in range(M):
        A, B = map(int,input().split())
        graph[A].append(B)
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
        for behind in graph[val]:
            indegree[behind] -= 1
            if indegree[behind] == 0: # 다 조건이 해제되었으니까 값을 넣어줌
                queue.append(behind)

    for val in result:
        print(val, end=" ")

if __name__ == "__main__":
    main()
'''
문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
입출력 예
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1


bfs를 이용해서 연결된거 연결하고 cnt+=1 노드별로 확인하면서 연결 안된 노드 있으면 다시 그거 기준으로 탐색하며 cnt+=1 반복하고 모든 노드 순회했을때 cnt 반환
유니온 파인드로도 가능

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a

def solution(n, computers):
    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(parent, i, j)

    networks = set()

    for i in range(n):
        networks.add(find(parent, i))

    return len(networks)
'''

from collections import deque

def bfs(computers, visited, start, n):
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()

        for next_node in range(n):
            if computers[current][next_node] == 1 and not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            bfs(computers, visited, i, n)
            answer += 1

    return answer
'''
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

좀 햇갈렸는데 부모를 저장하는 배열을 하나 두고, 여기에 연결된 자식 노드에 대해서 부모 노드가 뭐인지를 기록하면 됨.
이후 부모 노드 기록한 배열에서 2: 해서 출력.
'''

import sys 
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    graph = [[0] for _ in range(N+1)]
    parent = [0]*(N+1)
    
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # parent[1] = 0
    que = deque()
    que.append(1)

    # 부모 노드 배열에 연결된 자식노드를 찾고 그 자식노드의 부모가 무엇인지를 기록.
    while que:
        current = que.popleft()
        for v in graph[current]:
            if parent[v] == 0:
                parent[v] = current # 자신의 부모 노드에 대해서 기록
                que.append(v)
    
    print("\n".join(map(str, parent[2:])))
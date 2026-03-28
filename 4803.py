'''
입력은 여러 개의 테스트 케이스로 이루어져 있다. 
각 테스트 케이스의 첫째 줄에는 n ≤ 500과 m ≤ n(n-1)/2을 만족하는 정점의 개수 n과 간선의 개수 m이 주어진다. 
다음 m개의 줄에는 간선을 나타내는 두 개의 정수가 주어진다. 같은 간선은 여러 번 주어지지 않는다. 정점은 1번부터 n번까지 번호가 매겨져 있다. 입력의 마지막 줄에는 0이 두 개 주어진다.

입력으로 주어진 그래프에 트리가 없다면 "No trees."를, 
한 개라면 "There is one tree."를, 
T개(T > 1)라면 "A forest of T trees."를 테스트 케이스 번호와 함께 출력한다.

그래프 전체에서 트리가 몇 개인지 세는 문제라서,

아직 방문 안 한 정점 하나를 잡고
DFS/BFS로 그 정점이 속한 연결 요소 전체를 탐색
그 연결 요소가 트리인지 판별
트리면 개수 +1

이 연결 요소 안에 사이클이 있냐 없냐로 트리 판단.
이미 방문한 정점인데, 그게 부모 정점이 아니면 사이클
즉, 현재 정점 now에서 인접 정점 nxt를 볼 때

nxt == parent 이면 그냥 넘어감
visited[nxt] == True 이고 nxt != parent 이면 사이클 존재
'''

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append((start, 0))   # (현재 노드, 부모 노드) -> 추후 현재 노드에서 연결된 내용에서 자신의 부모 노드가 아닌데 방문한 노드로 갔다면, 사이클이기에 이를 파악하려고 부모 노드도 같이 넣음.
    visited[start] = True
    is_tree = True

    while queue:
        now, parent = queue.popleft()

        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, now))
            elif nxt != parent:
                is_tree = False

    return is_tree

if __name__ == "__main__":
    case = 1

    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        graph = [[] for _ in range(n+1)]
        visited = [False]*(n+1)

        for _ in range(m):
            a, b = map(int, input().split())
            # 무방향 그래프이니 둘다 넣어줌.
            graph[a].append(b)
            graph[b].append(a)

        tree_count = 0

        for i in range(1, n+1):
            if not visited[i]:
                if bfs(i):
                    tree_count += 1

        if tree_count == 0:
            print(f"Case {case}: No trees.")
        elif tree_count == 1:
            print(f"Case {case}: There is one tree.")
        else:
            print(f"Case {case}: A forest of {tree_count} trees.")
        case += 1
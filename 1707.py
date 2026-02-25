'''
각 노드별로 인접한 노드를 저장하는 2차원 리스트를 만들면 다음과 같이 된다. (0번 인덱스는 버리는 공간)
graph = [[], [2, 4], [1, 3], [2, 4], [1, 3]]

해당 노드를 방문했는지 아닌지, 방문 했다면 어떤 그룹에 속하는 지 나타내는 체크 리스트를 만든다. (0번 인덱스는 버리는 공간)
visited = [False, False, False, False, False]

False면 미방문, 서로 다른 그룹은 1, -1 
1번 노드부터 4번 노드까지 반복하는 for loop를 돌면서, 방문하지 않은 노드라면 BFS를 호출하면 된다. 그 과정에서 이분 안된다면 NO출력.
'''

from collections import deque
import sys

input = sys.stdin.readlines


def bfs(start, group, graph, visited):
    queue = deque()
    queue.append((start))
    visited[start] = group

    while queue:
        node = queue.popleft()

        for link_node in graph[node]:
            if not visited[link_node]:
                queue.append(link_node)
                visited[link_node] = -visited[node] # 인접 노드이니까 기존 노드와 부호 다르게 해서 다른 그룹으로 해서 넣음
            elif visited[link_node] == visited[node]: # 인접 노드가 방문을 했었는데 그 값이 지금 노드와 부호(그룹)같으면 지금 이분 그래프가 안되므로 False
                return False

    return True


def main():
    K = int(input())

    for test in range(K):
        V, E = map(int,input().split())
        graph = [[] for _ in range(V+1)]
        for edge in range(E):
            u, v = map(int,input().split())
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * (V+1)
        
        for i in range(1, V+1):
            if not visited[i]:
                result = bfs(i,1,graph,visited)
                if not result: # 이분그래프가 아니면 (false)
                    print("NO")
                    break
        else: # break가 안 나왔을 때 실행
            print("YES")

if __name__ == "__main__":
    main()

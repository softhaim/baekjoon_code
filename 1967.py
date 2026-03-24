'''
파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 
둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 

간선에 대한 정보는 세 개의 정수로 이루어져 있다. 
첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 
두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 
간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 
루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

첫째 줄에 트리의 지름을 출력한다.

트리에서 지름은 루트에서 가장 먼거 찾고 그 먼것에서 다시 가장 먼것 찾으면 됨.
'''
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    que = deque()
    que.append(start)
    dist = [-1]*(N+1)
    dist[start] = 0

    while que:
        node = que.popleft()
        for child_node, weight in tree[node]:
            if dist[child_node] == -1:
                que.append(child_node)
                dist[child_node] = dist[node] + weight

    max_dist = 0
    max_node = 1
    for i in range(1, N+1):
        if dist[i] > max_dist:
            max_dist = dist[i]
            max_node = i

    return max_node, max_dist

if __name__ == "__main__":
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        node, child_node, weight = map(int, input().split())
        tree[node].append((child_node, weight))
        tree[child_node].append((node,weight))
    
    max_node_start1, max_dist_start1 = bfs(1)
    max_node, max_dist = bfs(max_node_start1)

    print(max_dist)


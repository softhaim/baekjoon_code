'''
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

bfs해서 1번 정점에서 가장 먼 점 A를 찾고
A에서 가장 먼 점까지의 거리 찾으면 된다고 한다. 
트리에서 아무 정점에서 가장 먼 정점은 지름의 한 끝점이라 이 끝점 찾고 끝점에서 가장 먼것을 구하면 지름이 된다.
여러번 모든 정점에서 하는건 비효율이라 아닌거 같은데 접근을 어떻게 해야할지 몰라서 푸는 핵심만 컨닝좀 했다.
'''
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    dist = [-1]*(N+1)
    dist[start] = 0
    que = deque()
    que.append(start)

    while que:
        now = que.popleft()
        for nxt, val in graph[now]: # graph[now] == (nxt, cost)
            if dist[nxt] == -1:
                que.append(nxt)
                dist[nxt] = dist[now] + val

    max_dist = 0
    max_node = 1
    for i in range(1, N+1):
        if dist[i] > max_dist:
            max_dist = dist[i]
            max_node = i

    return max_dist, max_node


if __name__ == "__main__":
    N = int(input())

    graph = [[] for _ in range(N + 1)]    

    for _ in range(N):
        input_num = list(map(int, input().split()))
        node = input_num[0]
        idx = 1
        while input_num[idx] != -1:
            nxt = input_num[idx]
            cost = input_num[idx+1]
            graph[node].append((nxt, cost))
            idx += 2
    
    _, max_far_node1 = bfs(1)
    max_dist, max_far_node = bfs(max_far_node1)
    print(max_dist)
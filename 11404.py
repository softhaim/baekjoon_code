'''
다익스트라의 경우 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 알고리즘이다. 
그러나 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야하는 경우 플루이드워셜 알고리즘 사용하면 된다.
'''

import sys

input = sys.stdin.readline

INF = (1e9)

def floyd(graph):
    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if __name__ == "__main__":
    N = int(input()) # 도시의 개수
    M = int(input()) # 버스의 개수

    graph = [[INF]*(N+1) for _ in range(N+1)]
    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if a == b:
                graph[a][b] = 0

    for i in range(M):
        a,b,c = map(int, input().split())
        # graph[a][b] = c
        graph[a][b] = min(graph[a][b], c)

    floyd(graph)

    # 수행된 결과를 출력
    for a in range(1, N+ 1):
        for b in range(1, N + 1):
            if graph[a][b] == INF:
                print(0, end=' ')
            else:
                print(graph[a][b], end=' ')
        print()

    



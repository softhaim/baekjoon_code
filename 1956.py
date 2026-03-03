'''
다익스트라의 경우 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 알고리즘이다. 
그러나 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야하는 경우 플루이드워셜 알고리즘 사용하면 된다.
여기서도 모든 지점에 대해서 구하고 그 중에서 가장 작은 값 출력하는 것이니까 풀루이드워셜 씀.
플루이드:  112640kb	   1092ms
다익스트라: 212156kb	6216ms
'''

import sys

input = sys.stdin.readline

INF = (1e9)

def floyd():
    for k in range(1, V+1):
        for a in range(1, V+1):
            for b in range(1, V+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if __name__ == "__main__":
    V, E = map(int, input().split())

    graph = [[INF]*(V+1) for _ in range(V+1)]

    for a in range(V+1):
        for b in range(V+1):
            if a == b:
                graph[a][b] = 0

    for i in range(E):
        a,b,c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)
    
    floyd()
    answer = INF
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if i != j and graph[i][j] != INF and graph[j][i] != INF:
                answer = min(answer, graph[i][j] + graph[j][i])

    print(answer if answer != INF else -1)


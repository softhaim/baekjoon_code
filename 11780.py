'''
플루이드 워셜에서 경로 추적까지 하는것
이전 처럼 prev해서 이전 원소들 추적하는 것은 아니고 3차원?처럼 prev구성해서 [i][j]일때, 그때 k 이전의 paht와 k 이후의 path넣는식으로 하면서 path 를 구성하고 그 값을 저장하도록 함.
prev[i][j] = prev[i][k] + prev[k][j][1:]

이거 하고 저거 길이랑 값 출력하면 그만.
'''

import sys

input = sys.stdin.readline

INF = float('inf')

def floyd():
    
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i == j: continue
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j] 
                    prev[i][j] = prev[i][k] + prev[k][j][1:] # 1: 하는것이 k 까지의 path 를 넣으면서 k 가 들어갔고 k 이후 부터의 path를 넣으면서 k 가 중복되니까 하는것임.

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    graph = [[INF]*(N+1) for _ in range(N+1)]
    prev = [[()]*(N+1) for _ in range(N+1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, N + 1):
        graph[a][a] = 0

    for i in range(M):
        a,b,w = map(int,input().split())
        if graph[a][b] > w:
            graph[a][b] = w
            prev[a][b] = (a, b)

    floyd()
    
    for i in range(1,N+1):
        for j in range(1, N+1):
            print(graph[i][j] if graph[i][j] != INF else 0, end=" ")
        print()
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(len(prev[i][j]), *prev[i][j])
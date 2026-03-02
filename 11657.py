''''
음수 가중치 있는 그래프의 최단거리 찾는 문제 -> 다익스트라는 못쓰고 벨만포드 써야하는 문제임

벨만포드의 알고리즘은 

출발 노드를 설정한다.
최단 거리 테이블을 초기화한다.
다음의 과정을 노드개수-1번 반복한다.
전체 간선 E개를 하나씩 확인한다.
각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
→ 출발 노드가 방문한 적 없는 노드(출발거리 == INF)일 때 값을 업데이트 하지 않는다.
→ 출발 노드의 거리 리스트값 + 에지 가중치 < 종료 노드의 거리 리스트 값 일 때 종료 노드의 거리 리스트 값을 업데이트 한다.
만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번의 과정을 한 번 더 수행한다.
→ 이 때 최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재하는 것이다.

'''

import sys

input = sys.stdin.readline

INF = (1e9)

def bellman_ford(start):
    dist = [INF]*(N+1)
    dist[start] = 0
    # N-1 번 완화
    for i in range(N-1):
        updated = False
        for a, b, c in edge:
            if dist[a] != INF and dist[b] > dist[a] + c: # 출발노드 무한 아니고, 현재 도착 노드 값이 출발에서 c한 값보다 크면
                dist[b] = dist[a] + c
                updated = True
        if not updated: # 간선 갱신이 없다면 조기 종료
            break
    for a, b, c in edge: # 한번 더 해서 갱신이 된다면 그건 음수 가중치 사이클 있어서 계속 감소하는것임.
        if dist[a] != INF and dist[b] > dist[a] + c:
            return None
    return dist

if __name__ == "__main__":
    N, M = map(int,input().split())
    edge = []

    for i in range(M):
        a, b, c = map(int, input().split())
        edge.append((a,b,c))
        
    distance = bellman_ford(1)

    if distance == None:
        print(-1)
    else: # 각 줄에 1번 도시에서 출발해 2번 도시, 3번 도시, ..., N번 도시로 가는 가장 빠른 시간을 순서대로 출력
        for i in range(2, N+1):
            print(distance[i] if distance[i] != INF else -1)
'''
도시에 있는 모든 두 집 쌍에 대해, 불이 켜진 길만으로 서로를 왕래할 수 있어야 한다.

위 조건을 지키면서 절약할 수 있는 최대 액수를 구하시오.

최소 신장 트리 문제.
전체 비용 구해둔 후 최소 신장 트리의 비용 만큰 뺀 것이 절약 할 수 있는 최대 액수임.
'''

import sys

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
    return

if __name__ == "__main__":

    while True:
        M, N = map(int, input().split()) # 집의 수, 길의 수
        if M == 0 and N == 0: break 

        parent = [i for i in range(M)] # 자기 자신으로 대표 노드 초기화
        edge = []
        total_cost = 0 # 총액 저장 변수 -> 이후 이 값과 최소 신장 트리의 비용 빼서 절약한 금액 알 수 있도록 할 것임.
        for i in range(N):
            x, y, z = map(int, input().split()) # x번 집과 y번 집 사이에 양방향 도로가 있으며 그 거리가 z미터라는 뜻
            edge.append((z,x,y))
            total_cost += z

        edge.sort()
        min_cost_sum = 0
        for dist, x, y in edge:
            if find(x) != find(y):
                union(x, y)
                min_cost_sum += dist
        print(total_cost - min_cost_sum)
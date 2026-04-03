'''
별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

MST 문제. 각 거리를 계산해서 cost로 두고 크루스칼 하면 됨.
'''
import sys

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
    return

if __name__ == "__main__":
    N = int(input()) # 별들의 개수
    parent = [i for i in range(N+1)] # 각 입력 들어온 순서로 번호 매기고 각 별들의 집합 대표노드 자기 자신 초기화
    stars = dict() # i번째 입력의 별들 위치 저장
    for i in range(1,N+1):
        x, y = map(float, input().split()) # 별들의 좌표
        stars[i] = (x,y)
    
    # 크루스칼 위해서 가중치 순서로 정렬 -> 거리로 정렬
    edges = []
    for i in range(1, N+1):
        x1, y1 = stars[i]
        for j in range(i+1, N+1):
            x2, y2 = stars[j]
            dist = (abs(x2-x1)**2 + abs(y2-y1)**2)**(1/2)
            edges.append((dist, i, j))
    edges.sort()

    result = 0
    for dist, i, j in edges:
        if find(i) != find(j): # 대표 노드가 다르면 기존에 넣은것 아니고, 사이클 생기는 것도 아니기에 MST에 합침
            union(i, j)
            result += dist
    print(f"{result:.2f}")
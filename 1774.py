'''
이미 황선자씨와 연결된, 혹은 우주신들과 연결된 통로들이 존재한다. 우리는 황선자 씨를 도와 아직 연결이 되지 않은 우주신들을 연결해 드려야 한다. 새로 만들어야 할 정신적인 통로의 길이들이 합이 최소가 되게 통로를 만들어 “빵상”을 외칠수 있게 도와주자.
-> 최소 신장 트리 문제
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

if __name__ == "__main__":
    N, M = map(int, input().split()) # 우주신 개수, 통로의 개수
    parent = [i for i in range(N+1)] # 집합의 대표 노드 자기 자신 초기화

    space_god = [(0,0)]
    for i in range(N): # 우주신들 좌표
        x, y = map(int, input().split())
        space_god.append((x,y))

    for i in range(M): # 이미 연결된 통로 -> 이미 union 된 것이라고 보면 됨.
        a, b = map(int, input().split())
        union(a,b)

    edge = []

    for i in range(1, N): # 마지막꺼는 어차피 자기 자신 말고는 이을 거 없으니 뺌.
        x1, y1 = space_god[i]
        for j in range(i+1, N+1):
            x2, y2 = space_god[j]
            dist = (abs(x2-x1)**2 + abs(y2-y1)**2)**(1/2)
            edge.append((dist, i, j))

    edge.sort()

    result = 0
    for dist, i, j in edge:
        if find(i) != find(j):
            union(i,j)
            result += dist
    print(f"{result:.2f}")
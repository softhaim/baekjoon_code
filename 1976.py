'''
도시들의 개수와 도시들 간의 연결 여부가 주어져 있고, 동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때 가능한지 여부를 판별하는 프로그램을 작성하시오. 
같은 도시를 여러 번 방문하는 것도 가능하다.

-> 같은 도시 여러번 때문에 bfs 같은거는 아닐거고, 유니온 파인드로 해서 해당 도시들이 같은 집합인지로 여행 가능 여부 판단
'''

import sys

input = sys.stdin.readline

def find(num):
    if parent[num] != num: # 자기 자신이 대표가 아닐 때, 대표 노드로 갱신 및 찾음
        parent[num] = find(parent[num])
    return parent[num]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_b] = root_a
    return

if __name__ == "__main__":
    N = int(input()) # 도시의 수
    M = int(input()) # 여행 계획에 속한 도시 수

    parent = [i for i in range(N+1)]
    for i in range(1,N+1):
        graph_i = list(map(int, input().split()))

        for idx, val in enumerate(graph_i, 1):
            if val != 0: # 연결되어있으면,
                union(i, idx)
    travel_plan = list(map(int, input().split()))

    for i in range(1, M):
        if find(travel_plan[i-1]) != find(travel_plan[i]):
            print("NO")
            break
    else:
        print("YES")
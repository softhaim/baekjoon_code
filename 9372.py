'''
최소 신장 트리 문제. 유니온 파인드 하면서 최소 신장 트리 조건에 맞으면 넣음
원래 쿠르스칼알고리즘은 가중치로 먼저 정렬하고 그 다음에 순회하면서 넣어야 하는데 여긴 가중치는 없으니 그냥 유니온 파인드하고 맞으면 넣음. 
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
        if root_a > root_b:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a

if __name__ == "__main__":
    T = int(input())

    for t in range(T):
        N, M = map(int, input().split()) # 국가의 수, 비행기 종류
        parent = [i for i in range(N+1)]
        cnt = 0
        for i in range(M):
            a, b = map(int, input().split()) # a와 b를 왕복하는 비행기가 있다는 것
            if find(a) != find(b):
                union(a, b)
                cnt += 1
            else: # 사이클 생기면 안됨.
                continue
        print(cnt)
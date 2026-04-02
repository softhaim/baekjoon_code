'''
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.
최소 신장 트리 구하는 문제
아마도 크루스칼 쓰면 될듯
'''
import sys
sys.setrecursionlimit(10**5) # 없으면 recursion error

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

if __name__ == "__main__":
    V, E = map(int,input().split())
    parent = [i for i in range(V+1)]
    edge = []
    for i in range(E):
        a, b, c = map(int, input().split()) 
        edge.append((c,a,b)) # c 부터 넣는 이유는 정렬 시 a,b,c 면 key = lambda x : x[2] 해야하는데 c부터 넣으면 그냥 sort 하면 되니까 그냥 저렇게 함.

    edge.sort()
    result_cost = 0

    for val in edge:
        cost, now_a, now_b = val
        if find(now_a) != find(now_b):
            union(now_a, now_b)
            result_cost += cost
            
    print(result_cost)
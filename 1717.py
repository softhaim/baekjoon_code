'''
유니온 파인드(disjoint set) 문제라고 한다.
대표하나 설정해서 그것과 연결을 시켜두고, 이후 해당 대표값 기반으로 해당 원소랑 같은 대표라면 같은 집합이고 아니면 아닌거임.
'''

import sys

input = sys.stdin.readline

def find(num):
    # num 이 자기 자신이 대표가 아니면, 대표가 누구인지 찾음
    if parent[num] != num:
        parent[num] = find(parent[num]) # 경로 압축

    return parent[num]

def union(a, b):
    ''' 
    a, b의 집합 대표를 찾음.
    예를 들어 1, 2 하고 2,3 하면 둘다 집합대표 1 인 집합에 있다고 표시 하는 거임. 
    '''
    root_a = find(a)
    root_b = find(b)

    # 대표가 서로 다르면 합침
    if root_a != root_b:
        parent[root_b] = root_a

if __name__ == "__main__":
    n ,m = map(int, input().split())
    parent = [i for i in range(n+1)] # 해당 인덱스의 값 원소 대한 대표 노드 설정. 초기는 자기 자신으로 설정.
    for _ in range(m):
        op, a, b = map(int, input().split())
        
        if op == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")
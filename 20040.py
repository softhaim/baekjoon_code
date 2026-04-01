'''
매 차례 마다 플레이어는 두 점을 선택해서 이를 연결하는 선분을 긋는데, 이전에 그린 선분을 다시 그을 수는 없지만 이미 그린 다른 선분과 교차하는 것은 가능하다. 
게임을 진행하다가 처음으로 사이클을 완성하는 순간 게임이 종료된다.

C에 속한 임의의 선분의 한 끝점에서 출발하여 모든 선분을 한 번씩만 지나서 출발점으로 되돌아올 수 있다.

서로 다른 두 점이 주어질 때마다 그 두 점을 union 함수를 이용하여 합치고, 만일 그 두 점의 root가 같으면 사이클이 생긴 것이므로 탐색을 종료
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
    n, m = map(int, input().split())
    parent = [i for i in range(n)]
    result = 0
    for i in range(1,m+1):
        a, b = map(int, input().split())
        if find(a) == find(b):
            print(i)
            break
        union(a,b)
    else:
        print(0)
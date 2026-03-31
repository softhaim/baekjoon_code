'''
유니온 파인드 문제
유니온 파인드로 딕셔너리로해서 대표를 저장하도록 하면서 누구의 집합안에 있는지 알 수 있게 함.
이 과정에서 num을 저장하도록 함. union하면서 루트 달라서 합치면 그 합친 대표의 num 을 합치고자 하는 것의 num과 합쳐서 대표의 num이 집합에 있는 사람 수
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
        parent[root_b] = root_a
        friend_num[root_a] += friend_num[root_b]
    print(friend_num[root_a])

if __name__ == "__main__":
    T = int(input()) # 테스트 케이스
    
    for t in range(T):
        F = int(input()) # 친구의 관계 수
        parent = dict()
        friend_num = dict()
        for _ in range(F):
            friend1, friend2 = input().split()
            if friend1 not in parent:
                parent[friend1] = friend1
                friend_num[friend1] = 1
            if friend2 not in parent:
                parent[friend2] = friend2
                friend_num[friend2] = 1
            union(friend1, friend2)
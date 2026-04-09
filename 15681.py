'''
트리의 정점의 수 N과 루트의 번호 R, 쿼리의 수 Q가 주어진다. (2 ≤ N ≤ 105, 1 ≤ R ≤ N, 1 ≤ Q ≤ 105)

이어 N-1줄에 걸쳐, U V의 형태로 트리에 속한 간선의 정보가 주어진다. (1 ≤ U, V ≤ N, U ≠ V)

이는 U와 V를 양 끝점으로 하는 간선이 트리에 속함을 의미한다.

이어 Q줄에 걸쳐, 문제에 설명한 U가 하나씩 주어진다. (1 ≤ U ≤ N)

처음엔 bfs로 순회하면서 tree를 만들고 이 트리를 바탕으로 아래 노드 수를 계산하려 했는데 어차피 이러면 dfs를 통하여 들어가서 리프에서 1 반환하고, 이를 부모 노드쪽에서 리턴 값을 += 해서 합하여 저장하여 자식 몇개 있는지 기록하면 됨.
따라서 dfs를 구현해서 트리를 기반으로 부모 노드 아닐때 dfs로 들어가고, 리프이면 1만 저장 후 종료 혹은 반환하게 하고 이를 부모 노드 스택쪽에 돌아오면 이 값들을 합해서 몇개 자식 있는지 합해놓으면 된다.
'''
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(node, parent):
    subtree[node] = 1 # 자기 자신 포함
    for nxt in tree[node]:
        if nxt != parent:
            dfs(nxt, node)
            subtree[node] += subtree[nxt]
        

if __name__ == "__main__":
    N, R, Q = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    for i in range(N-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    subtree = [0] * (N + 1)
    dfs(R, 0)

    for _ in range(Q):
        U = int(input())
        print(subtree[U])
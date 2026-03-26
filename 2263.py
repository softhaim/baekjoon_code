'''
n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.

inorder 는 왼 루트 오
postorder 는 왼 오 루트
preorder 는 루트 왼 오

후위 순위 리스트의 마지막 원소가 루트노드가 되며, 이를 출력한다.
중위 순위 리스트에서 루트노드의 왼쪽이 왼쪽자식, 오른쪽이 오른쪽 자식이 된다.

이를 원소가 하나 남을 때까지 반복한다.
원소가 하나라면 자기 자신밖에 없으므로 그대로 출력
'''
import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

def pre_order(in_start, in_end, post_start, post_end):
    if in_start > in_end:  # 리프 노드
        return 
    root = post_order[post_end]
    idx_root = pos[root]
    offset = idx_root - in_start # 왼쪽 서브트리 노드 수
    print(root, end=" ")

    # left_nodes = in_order[:idx_root]
    # left_nodes_post = post_order[:idx_root]
    # right_nodes = in_order[idx_root+1:]
    # right_nodes_post = post_order[idx_root:len-2] # inorder에서 루트 위치만 빠진거니까 저 중위에서 루트 인덱스부터 오른쪽 자식 시작해서 마지막 루트 위치 뺌.

    pre_order(in_start, idx_root-1, post_start, post_start+offset-1) # 왼쪽
    pre_order(idx_root+1, in_end, post_start+offset, post_end-1) # 오른쪽

if __name__ == "__main__":
    N = int(input())

    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))

    pos = [0] * (N + 1)
    for i, v in enumerate(in_order):
        pos[v] = i

    pre_order(0,N-1,0,N-1)
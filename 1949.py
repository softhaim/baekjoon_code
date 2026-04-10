import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
'''
같은 부분문제가 반복되면 저장해서 재사용 -> dp
dfs로 dp 로 만들어둔 것을 바탕으로 모든 경우의 수에 따라서 dfs로 들어가면서 선택했을 경우, 자기 자신의 값으로 초기화 해둠. 
이후 리프노드 까지 방문하면 dfs를 빠져나오면서 차례로 현재 노드의 선택한 경우 각각에 대해서 자식 노드의 선택따른 max 합을 저장. 
우수 마을이면 자식은 우수마을이면 안되니까 우수마을로 안한 경우일때 값을 더하고, 현재가 우수마을 아니면 자식은 어떤 값을 선택하든 큰 값이기만 하면 되니까 둘 중 하나 max로 골라서 sum 함.
그렇게 위로 올라오면서 1(루트노드)에서 최종적으로 루트에서 우수 노드로 선택한 경우, 안한 경우 대해서 max 하면 됨
'''
def dfs(node, parent):
    dp[node][1] = num_human[node]  # node를 우수마을로 선택
    dp[node][0] = 0                # node를 우수마을로 선택 안 함

    for nxt in tree[node]:
        if nxt == parent:
            continue

        dfs(nxt, node)

        # 현재 노드가 우수마을이면 자식은 우수마을이면 안 됨
        dp[node][1] += dp[nxt][0]

        # 현재 노드가 우수마을이 아니면 자식은 둘 중 큰 값 선택 가능
        dp[node][0] += max(dp[nxt][0], dp[nxt][1])

if __name__ == "__main__":
    N = int(input())
    num_human = [0] + list(map(int, input().split())) # 1-index 위해서 앞 0 추가
    tree = [[] for _ in range(N + 1)]
    dp = [[0, 0] for _ in range(N + 1)] # 우수 노드로 선정하는 경우와 아닌 경우에 대해서 노드별로 기록 가능하도록 구성

    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    dfs(1, 0)
    print(max(dp[1][0], dp[1][1]))
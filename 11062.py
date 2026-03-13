'''
한 턴에는 가장 왼쪽에 있는 카드나 가장 오른쪽에 있는 카드를 가져갈 수 있다. 카드가 더 이상 남아있지 않을 때까지 턴은 반복된다. 게임의 점수는 자신이 가져간 카드에 적힌 수의 합이다.

결국 왼쪽 아님 오른쪽 골랐을때 dfs로 해서 왼/오 따른 경우의 수를 저장해두고 이 중 max출력하면 됨.
'''

import sys

input = sys.stdin.readline

def dfs(left, right):
    if left > right:
        return 0
    if dp[left][right] != -1: # 이미 기록된 경우 재사용
        return dp[left][right]

    # 내가 왼쪽 가져가면 다음에는 상대턴 이므로 상대가 내 점수를 최소화하도록 움직임. -> min이라는것이 핵심인듯. 이걸 몰랐음.
    take_left = card[left] + min(dfs(left+2, right), dfs(left+1, right-1)) # left+2 는 상대가 left를 가져갔을때의 나의 차례일때 내가 왼쪽 상대 왼쪽으로 왼쪽 2장이 없어짐. 반대는 오른쪽 가져간 경우
    take_right = card[right] + min(dfs(left+1,right-1), dfs(left,right-2))
    dp[left][right] = max(take_left, take_right)

    return dp[left][right]

if __name__ == "__main__":
    T = int(input())

    for t in range(T):
        N = int(input())
        card = [0]+list(map(int,input().split()))

        is_my_turn = True
        sum_result = 0
        dp = [[-1]*(N+1) for i in range(N+1)] # 1, N 일때. 즉, 카드를 전체 사용했을때 값을 출력 하도록 저장하는 dp 각 내가 뽑을 수 있는 카드에서 카드를 뽑았을때의 max값을 저장. 
        print(dfs(1,N))
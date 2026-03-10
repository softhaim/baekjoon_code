import sys
# sys.setrecursionlimit(10**3) # 필요시 주석 해제
input = sys.stdin.readline

def dfs(idx, diff):
    # 이미 방문한 상태면 다시 볼 필요 없음
    if dp[idx][diff]:
        return
    
    dp[idx][diff] = True

    # 모든 추를 다 봤으면 종료
    if idx == num_chu:
        return

    w = chu_weight_arr[idx]

    # 1. 현재 추를 사용하지 않는 경우
    dfs(idx + 1, diff)

    # 2. 현재 추를 한쪽에 올려서 차이가 커지는 경우
    dfs(idx + 1, diff + w)

    # 3. 현재 추를 반대쪽에 올려서 차이가 줄어드는 경우
    dfs(idx + 1, abs(diff - w))

if __name__ == "__main__":
    num_chu = int(input())

    chu_weight_arr = list(map(int, input().split()))

    marble_num = int(input())

    marble_weight_arr = list(map(int, input().split()))

    # 추의 총합보다 큰 구슬은 절대 측정 불가
    max_weight = sum(chu_weight_arr)

    # dp[idx][diff] =
    # idx번째 추까지 고려했을 때, 무게 차이 diff를 만들 수 있는지 여부
    dp = [[False] * (max_weight + 1) for _ in range(num_chu + 1)]

    # 처음에는 아무 추도 안 썼고, 차이는 0
    dfs(0, 0)

    # 각 구슬에 대해 측정 가능한지 확인
    for marble in marble_weight_arr:
        if marble > max_weight:
            print("N", end=" ")
        elif dp[num_chu][marble]:
            print("Y", end=" ")
        else:
            print("N", end=" ")
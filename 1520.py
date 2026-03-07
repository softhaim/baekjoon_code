'''
이건 dfs 로 경로를 끝까지 들어가보면서 찾으면 1 반환하고 돌아가면서 해당 경로에 1씩 +를 함. 그 과정에서 기존에도 탐색했던 경로라면 그 경로 따라가게 될거니까 해당 경우의 수에서 +1 해주면 됨
그렇게 해서 0,0 에서는 경우의 수의 dfs가 반환한 수의 합을 저장하게 하면 됨. 이 과정에서 기존에 탐색했다면 기존 값 반환을 위해 dp 사용. 
'''
import sys 
sys.setrecursionlimit(10**4)  # 재귀 호출이 많아질 수 있으므로 제한 늘림 -> 이거 안하니까 (RecursionError) 발생함. 10**6 은 또 메모리 초과이길래 줄여봄. 4승이 통과 되고 3은 에러남.
input = sys.stdin.readline

def dfs(x,y):
    # 도착점에 도달했으면 경로 1개
    if x == M-1 and y == N-1:
        return 1
    # 이미 계산한 칸이면 저장값 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 처음 이 칸 계산이므로 일단 방문했으니 0 으로 초기화.
    dp[x][y] = 0

    # 상하좌우 탐색
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0<=nx<M and 0<=ny<N and map_arr[nx][ny] < map_arr[x][y]: # 현재보다 낮으면 내려감
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

if __name__ == "__main__":

    M, N = map(int, input().split()) # 행개수, 열개수

    map_arr = []

    for i in range(M):
        map_arr.append(list(map(int, input().split())))

    dx = [-1,0,0,1]
    dy = [0,1,-1,0]

    dp = [[-1]*N for _ in range(M)]

    print(dfs(0,0))
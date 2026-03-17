'''
딱히 그래프도 아니고 최단 거리 찾는건데 그렇기에 bfs로 시작 두 지점 대해서 bfs해서 각 지점에서의 최단거리를 찾음. 튜플로 넣으면서 (x,y,number) 해서 넣고 그렇게 x,y가 현재 찾는위치라면,
그때의 최솟값과 그때 경찰차 넘버 반환. 저 반환한 최솟값 합과 경찰차 넘버를 차레로 출력하면 될것이라 생각함.

=> 제출시 시간 초과 뜸. 문제가 장애물 같은거 없어서 그냥 가면 되니까 굳이 bfs를 안해도 되는듯? 그래서 시간 오래 걸려서 안되는거 같음.
그냥 단순하게 맨해튼 거리로 해서 abs해서 거리를 계산하고 그 위치부터해서 목적지까지 누가 가까운지만 체크하면 됨.
핵심은 이렇게 되면 사건별로 볼것이기에 dp 등을 사건의 개수로 맞추어 두고 이 사건에 따라서 거리를 계산해서 가까운 얘한테 줆.
그렇기에 현 상황에서 사건을 맡는 경우 생각하고 distance를 재귀적으로 들어가서 i번째와 j번째 수행해서 머물러있다는 전제하에 누가 더 가까운지 체크하고 가까운거의 거리와 번호 기록.
재귀 빠져나오면 그 전 단계 상황일거고 반환된 값은 둘다 동일하게 그 이후 상황에서의 최소 길이 반횐 될테니 비교 되는 값은 현재 거기까지 가는 비용 가지고 체크함. 그래서 가까운거로 기록

즉, 각 사건을 독립적으로 가장 가까운 경찰차에 배정하는 그리디 방식은 이후 사건들의 배정에 영향을 주므로 최적해를 보장하지 않는다. 
따라서 dp[i][j]를 “경찰차 1이 i번 사건, 경찰차 2가 j번 사건을 마지막으로 처리한 상태에서 남은 사건들을 처리하는 최소 이동거리”로 정의하고, 
다음 사건 nxt=max(i,j)+1을 경찰차 1이 맡는 경우와 경찰차 2가 맡는 경우를 모두 비교하는 DP로 해결해야 한다.
'''

import sys
# from collections import deque

input = sys.stdin.readline

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def bfs(end_x, end_y):
#     que = deque()
#     map_arr = [[0]*(N+1) for _ in range(N+1)]
#     que.append((1,1,1))
#     que.append((N,N,2))
#     map_arr[1][1] = 0
#     map_arr[N][N] = 0

#     while que:
#         nx, ny, police_num = que.popleft()
#         if nx == end_x and ny == end_y:
#             return map_arr[nx][ny], police_num

#         for i in range(4):
#             x = nx + dx[i]
#             y = ny + dy[i]
#             if 0<x<=N and 0<y<=N and map_arr[x][y] == 0:
#                 map_arr[x][y] = map_arr[nx][ny] + 1
#                 que.append((x,y,police_num))

def distance(a, b): # a 좌표 부터 b 좌표의 거리 구하는 것
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_pos1(i):
    if i == 0:
        return (1, 1)
    return cases[i]

def get_pos2(i):
    if i == 0:
        return (N, N)
    return cases[i]

# 상태 (i, j)에서 남은 사건들을 처리하는 최소 이동거리
def solve(i, j):
    if max(i, j) == W:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    nxt = max(i, j) + 1

    # 다음 사건을 경찰차 1이 처리
    move1 = distance(get_pos1(i), cases[nxt]) + solve(nxt, j)

    # 다음 사건을 경찰차 2가 처리
    move2 = distance(get_pos2(j), cases[nxt]) + solve(i, nxt)

    # i, j 상황에서의 다음 사건의 최소 거리 해당하는 길이와 다음 사건 누가 맡는지 기록
    if move1 <= move2: 
        dp[i][j] = move1
        trace[i][j] = 1
    else:
        dp[i][j] = move2
        trace[i][j] = 2

    return dp[i][j]

if __name__ == "__main__":
    N = int(input())
    W = int(input())

    cases = [None]  
    for _ in range(W):
        x, y = map(int, input().split())
        cases.append((x, y))

    # 경찰차 1이 i번째 사건까지 처리하고 현재 그 위치에 있음 경찰차 2가 j번째 사건까지 처리하고 현재 그 위치에 있음
    dp = [[-1] * (W + 1) for _ in range(W + 1)]
    trace = [[0] * (W + 1) for _ in range(W + 1)]

    print(solve(0, 0))

    i, j = 0, 0
    while max(i, j) < W:
        who = trace[i][j]
        print(who)
        nxt = max(i, j) + 1
        if who == 1: # trace는 현재 i,j상황에서 다음 누가 맡는지 기록하는것이기에 처음 0,0 에서는 첫 사건을 누가맡았는지 기록 되었을 것이고, 이 값 바탕으로 1이 했으면 i+1, 아니면 j+1 하고 그 위치에서 또 다음 사건은 누가맡는지 출력하고 다음 상황 이동.
            i = nxt
        else:
            j = nxt

    # end_idx = []
    # for w in range(W):
    #     a,b = map(int, input().split())
    #     end_idx.append((a,b))
    
    # sum_move_len = 0
    # police_number_arr = []
    # for val in end_idx:
    #     move_length, police_number = bfs(val[0],val[1])
    #     sum_move_len += move_length
    #     police_number_arr.append(police_number)

    # print(sum_move_len)
    # for val in police_number_arr:
    #     print(val)
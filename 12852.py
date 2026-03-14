'''
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

'''
import sys
from collections import deque
# sys.setrecursionlimit(10**5)

input = sys.stdin.readline

# 역시나 dfs 하면서 queue 하는 것이 시간이 오래걸려서 안됨.
# def dfs(n, queue):
#     global min_path
    
#     if n == 1:
#         if min_path == [] or len(queue) < len(min_path):
#             min_path = []
#             for i in range(len(queue)):
#                 min_path.append(queue[i])
#         return
    
#     if n % 3 == 0 and (dp[n//3] == 0 or dp[n//3]>dp[n]+1):
#         dp[n//3] = dp[n] + 1
#         queue.append(n//3)
#         dfs(n//3, queue)
#         queue.pop()
        
#     if n % 2 == 0 and (dp[n//2] == 0 or dp[n//2]>dp[n]+1):
#         dp[n//2] = dp[n] + 1
#         queue.append(n//2)
#         dfs(n//2, queue)
#         queue.pop()
        
#     if n > 1 and (dp[n-1] == 0 or dp[n-1]>dp[n]+1):
#         queue.append(n-1)
#         dp[n-1] = dp[n] + 1
#         dfs(n-1, queue)
#         queue.pop()

# 결국은 최단 거리 찾는거고 그 과정만 출력하도록 추가하는 로직이 있으면 됨.
def bfs(n):
    queue = deque()
    queue.append((N))
    dp[n] = 0

    while queue:
        x = queue.popleft()
        if x == 1: # 정답이 여러 가지인 경우에는 아무거나 출력한다. 이므로 최단거리 찾았으면 그거 출력하면 됨.
            return
        for nx in ( x//3 if x % 3 == 0 else -1,
                    x//2 if x % 2 == 0 else -1,
                    x-1):
            if nx != -1 and dp[nx] == -1:
                dp[nx] = dp[x] + 1
                prev[nx] = x
                queue.append(nx)

N = int(input())

dp = [-1]*(N+1)
prev = [-1]*(N+1)

cursor = 1
min_path = [1]

bfs(N)
print(dp[1])
while cursor != -1:
    min_path.append(prev[cursor])
    cursor = prev[cursor]
    
for i in range(len(min_path)-1, 0, -1):
    print(min_path[i-1], end=" ")

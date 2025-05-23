# 2075. N번째 큰 수
import sys, heapq

input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    arr_row = list(map(int, input().split()))
    
    if len(arr) >= n:
        for j in arr_row:
            if arr[0] < j: # 현재 최소값보다 크면 넣어줌
                heapq.heappop(arr)
                heapq.heappush(arr, j)
    else:
        for j in arr_row:
            heapq.heappush(arr, j)
    
# 모든 수는 자신의 한 칸 위에 있는 수보다 큼 => 근데 최댓값 찾아야 함
# 맥스힙 구조 만들어서 n 번째 값 뽑으면 됨.

# 위 처럼 arr의 최솟값보다 큰 수가 들어오면 최솟값을 빼고 새로운 수를 넣어줌
# 이렇게 하면 arr는 가장 큰 N개의 수만 들어가게 됨.

# 최종적으로 arr의 구조가 min heap이라 첫번째 요소가 n 번째로 큰수가 됨. (저 라이브러리가 최대 힙이 안됨. 하려면 음수로 넣고 다시 부호 바꾸는 식으로 출력해야함.)
print(arr[0])

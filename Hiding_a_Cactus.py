'''
문제 설명
m개의 행과 n개의 열로 구성된 격자가 주어지며, 이는 사막 지도를 나타냅니다. 사막 지도의 가장 왼쪽 위칸 좌표는 (0, 0), 오른쪽 아래칸 좌표는 (m-1, n-1)입니다. 이 사막 어딘가에 가로 w, 세로 h 크기의 선인장 구역을 조성하려 합니다. 선인장 구역은 격자 축에 맞춘 연속된 w × h 크기의 부분 격자이며, 회전할 수 없습니다.

비구름은 미리 정해진 순서대로 격자의 여러 칸에 비를 뿌립니다. 이때 빗방울이 처음으로 선인장 구역에 포함된 칸에 떨어졌을 때, 그 시점을 선인장이 처음으로 비를 맞는 순간으로 기록합니다. 당신은 선인장이 가능한 한 늦게 비를 맞도록, 선인장 구역의 위치를 정하려고 합니다.

선인장이 비를 맞지 않도록 선인장 구역의 위치를 정할 수 있다면 해당 위치가 가장 우선됩니다.
가능한 늦게 비를 맞는 선인장 구역 후보가 여러 개라면 그중 가장 위쪽 행, 그래도 여러 개면 가장 왼쪽 열에 위치한 구역을 선택합니다.
격자의 세로 길이와 가로 길이를 나타내는 정수 m, n, 선인장 구역의 세로 길이와 가로 길이를 나타내는 정수 h, w, 그리고 빗방울이 떨어지는 순서대로 칸의 좌표를 담은 2차원 정수 배열 drops가 매개변수로 주어집니다. 주어진 조건을 만족하는 선인장 구역에 포함된 가장 왼쪽 위칸의 좌표를 정수 배열로 return 하도록 solution 함수를 완성해 주세요.

제한사항
1 ≤ m, n ≤ 500,000
1 ≤ m × n ≤ 500,000
1 ≤ h ≤ m
1 ≤ w ≤ n
1 ≤ drops의 길이 ≤ m × n
drops[i]는 [r, c] 형태입니다.
drops[i]는 i + 1번째로 떨어진 빗방울의 좌표를 의미합니다.
0 ≤ r < m
0 ≤ c < n
drops의 모든 원소는 서로 다른 칸을 나타냅니다.
테스트 케이스 구성 안내
아래는 테스트 케이스 구성을 나타냅니다. 각 그룹은 하나 이상의 하위 그룹으로 이루어져 있으며, 하위 그룹의 모든 테스트 케이스를 통과하면 해당 그룹에 할당된 점수를 획득할 수 있습니다.

그룹	총점	추가 제한 사항
#1	30%	m ≤ 50, n ≤ 50
#2	70%	추가 제한 없음
입출력 예
m	n	h	w	drops	result
4	5	2	2	[[0, 0], [3, 1], [1, 3], [2, 4], [1, 1], [2, 2], [2, 3], [0, 4]]	[2, 2]
3	3	1	1	[[0, 0], [0, 1], [0, 2], [1, 0]]	[1, 1]
4	6	3	4	[[1, 2]]	[0, 0]
4	6	1	2	[[0, 1], [0, 3], [0, 5], [1, 1], [1, 3], [1, 5], [2, 1], [2, 3], [2, 5], [3, 1], [3, 3], [3, 5]]	[3, 4]
2	2	2	2	[[0, 0], [0, 1], [1, 1], [1, 0]]	[0, 0]
4	4	3	1	[[2, 0], [1, 3], [3, 2], [0, 1]]	[0, 2]


슬라이딩 윈도우로 푸는 문제. 정말 어려웠다. gpt 로 보고 푸는데도 뭔소리인지 잘 몰라서 한참 해맸다. 
'''

from collections import deque 
'''
dq는 현재 윈도우 안에서 최솟값 후보만 저장한다.
dq[0]은 항상 현재 윈도우의 최솟값이다.
i >= k-1일 때부터 윈도우가 완성되므로 결과를 저장한다.
'''
def sliding_min(arr, k):
    dq = deque()
    result = []
    
    for i, value in enumerate(arr):
        # 1. 현재 값보다 큰 값은 뒤에서 제거
        # 어차피 현재 값이 더 작고 더 늦게 들어왔으므로,
        # 앞의 큰 값들은 앞으로 최소값이 될 일이 없음
        while dq and dq[-1][1] >= value:
            dq.pop()
            
        dq.append((i, value))

        # 2. 윈도우 범위를 벗어난 값 제거
        while dq and dq[0][0] <= i - k:
            dq.popleft()

        # 3. 윈도우 크기가 k 이상이 된 순간부터 최솟값 기록
        if i >= k - 1:
            result.append(dq[0][1])

    return result
    
def solution(m, n, h, w, drops):
    INF = 10**18

    # rain_time[r][c] = 해당 칸에 비가 떨어지는 순서
    rain_time = [[INF] * n for _ in range(m)]

    for i, (r, c) in enumerate(drops):
        rain_time[r][c] = i + 1
        
    # 원래 격자에서 (i, j)를 왼쪽 위로 하는 h x w 직사각형의 최소 비 시간
    row_min = []
    for r in range(m):
        row_min.append(sliding_min(rain_time[r], w))
    
    width_count = n - w + 1
    best_time = 0
    answer = None
    # 세로 h칸 최솟값을 볼 열 개수: n-w+1 -> 5라고 하면, 3개씩 윈도우로 볼때 3번 보게됨.
    for c in range(width_count):
        col_values = []
        
        for r in range(m):
            col_values.append(row_min[r][c])
            
        col_min = sliding_min(col_values, h)
        
        # col_min[r] = (r, c)를 왼쪽 위로 하는 h x w 영역의 최소 비 시간
        for r, value in enumerate(col_min):
            if value > best_time:
                best_time = value
                answer = [r, c]
            elif value == best_time: # 동률이면 가장 더 왼쪽 위인거로
                if r < answer[0] or (r == answer[0] and c < answer[1]):
                    answer = [r, c]
                
    return answer
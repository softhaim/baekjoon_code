#20125

'''
머리는 심장 바로 윗 칸에 1칸 크기로 있다. 왼쪽 팔은 심장 바로 왼쪽에 붙어있고 왼쪽으로 뻗어 있으며, 
오른쪽 팔은 심장 바로 오른쪽에 붙어있고 오른쪽으로 뻗어있다. 허리는 심장의 바로 아래 쪽에 붙어있고 아래 쪽으로 뻗어 있다. 
왼쪽 다리는 허리의 왼쪽 아래에, 오른쪽 다리는 허리의 오른쪽 아래에 바로 붙어있고, 각 다리들은 전부 아래쪽으로 뻗어 있다.
각 신체 부위들은 절대로 끊겨있지 않으며 굽혀진 곳도 없다. 또한, 허리, 팔, 다리의 길이는 1 이상이며, 너비는 무조건 1이다.

쿠키의 신체가 주어졌을 때 심장의 위치와 팔, 다리, 허리의 길이를 구하여라.
'''

'''
첫 번째 줄에는 심장이 위치한 행의 번호 x와 열의 번호 y를 공백으로 구분해서 출력한다.

두 번째 줄에는 각각 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리의 길이를 공백으로 구분해서 출력하여라.
'''
'''
5 ≤ N ≤ 1,000. N은 판의 한 변의 길이를 의미하는 양의 정수다.
ai,j는 * 또는 _이다. *는 쿠키의 신체 부분이고, _는 쿠키의 신체가 올라가 있지 않은 칸을 의미한다. (1 ≤ i, j ≤ N)
쿠키의 신체 조건에 위배되는 입력은 주어지지 않는다.
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input().rstrip())) for _ in range(N)]
heart_row = None
heart_column = None

left_arm = 0
right_arm = 0
mid = 0
left_leg = 0
right_leg = 0

for idx, row in enumerate(arr):
    if '*' in row:
        # * 처음 발견한 곳이 머리 -> 이 한칸 아래 row 가 심장임.
        heart_row = idx + 1
        heart_column = row.index('*')
        break
# 여기서 팔길이 계산
start_left_arm_idx = arr[heart_row].index('*') # 첫 * 인덱스
left_arm = arr[heart_row][start_left_arm_idx:heart_column].count('*')
right_arm = arr[heart_row][heart_column+1:].count('*')

start_leg_idx = 0
left_leg_coulmn = 0
right_leg_coulmn = 0

for idx, row in enumerate(arr[heart_row+1:],1):
    #이제 * 2개 나오는 곳 찾아야 함. => 여기서부터 다리이기에, 그전은 허리이고, 그 다음부터 다리
    if row.count('*') == 2:
        mid = idx-1 #다리 전까지가 허리이기에
        start_leg_idx = idx+heart_row
        left_leg_coulmn = row.index('*')
        right_leg_coulmn = row.index('*', left_leg_coulmn+1)
        break

for idx, row in enumerate(arr[start_leg_idx:]):
    if row.count('*') == 2:
        right_leg += 1
        left_leg += 1
    elif row.count('*') == 1:
        if row.index('*') > left_leg_coulmn:
            right_leg += 1
        elif row.index('*') == left_leg_coulmn:
            left_leg += 1


print(heart_row+1, heart_column+1)
print(left_arm, right_arm, mid, left_leg, right_leg)

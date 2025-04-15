# 2304

'''
문제
N 개의 막대 기둥이 일렬로 세워져 있다. 기둥들의 폭은 모두 1 m이며 높이는 다를 수 있다. 이 기둥들을 이용하여 양철로 된 창고를 제작하려고 한다. 창고에는 모든 기둥이 들어간다. 이 창고의 지붕을 다음과 같이 만든다.

지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
지붕의 가장자리는 땅에 닿아야 한다.
비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.
그림 1은 창고를 옆에서 본 모습을 그린 것이다. 이 그림에서 굵은 선으로 표시된 부분이 지붕에 해당되고, 지붕과 땅으로 둘러싸인 다각형이 창고를 옆에서 본 모습이다. 이 다각형을 창고 다각형이라고 하자.

그림1 . 기둥과 지붕(굵은 선)의 예

창고 주인은 창고 다각형의 면적이 가장 작은 창고를 만들기를 원한다. 그림 1에서 창고 다각형의 면적은 98 ㎡이고, 이 경우가 가장 작은 창고 다각형이다.

기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.

입력
첫 줄에는 기둥의 개수를 나타내는 정수 N이 주어진다. N은 1 이상 1,000 이하이다. 그 다음 N 개의 줄에는 각 줄에 각 기둥의 왼쪽 면의 위치를 나타내는 정수 L과 높이를 나타내는 정수 H가 한 개의 빈 칸을 사이에 두고 주어진다. L과 H는 둘 다 1 이상 1,000 이하이다.

출력
첫 줄에 창고 다각형의 면적을 나타내는 정수를 출력한다.
'''
'''
해결 방법
x축 순으로 기둥을 정렬한 후 가장 높은 기둥을 알아낸다.
가장 왼쪽의 기둥 높이를 기준으로 가장 높은 기둥 전까지 면적을 계속 더하는데, 현재 기둥보다 다음 기둥이 더 작으면 기준의 높이를 더해주고 다음 기둥이 더 크다면 기준이 되는 높이를 갱신한다.
오른쪽에서부터도 똑같이 온다.
'''
import sys

input = sys.stdin.readline

N = int(input())

house = []
for i in range(N):
    house.append(list(map(int, input().split())))

house.sort(key=lambda x: x[0])
max_height = max(house, key=lambda x: x[1])
global_max_height_index = house.index(max_height)
area = 0


# 왼쪽 기둥들
max_height_value = house[0][1] 
max_height_index = 0
for i in range(global_max_height_index):
    if max_height_value < house[i + 1][1]: # 다음 기둥이 더 크면
        area += (house[i + 1][0] - house[max_height_index][0]) * max_height_value # x축 길이 * 기준 높이
        # print(area)
        max_height_value = house[i + 1][1]
        max_height_index = i + 1 # 기준 기둥 갱신
    else:
        continue
# 오른쪽 기둥들
max_height_value = house[-1][1]
max_height_index = -1
for i in range(N-1, global_max_height_index, -1):
    if max_height_value < house[i - 1][1]: # 다음 기둥이 더 크면
        area += (house[max_height_index][0] - house[i-1][0]) * max_height_value # x축 길이 * 기준 높이
        # print(f'max_index:{house[max_height_index][0]}, x_val:{house[max_height_index][0] - house[i][0]}, height:{max_height_value}' )
        # print(area)
        max_height_value = house[i - 1][1]
        max_height_index = i - 1
    else:
        continue
    
# 중앙 가장 큰 기둥 구간 처리 -> 이 부분이 틀렸었음.
max_h = max(house, key=lambda x: x[1])[1]
max_pillars = [x for x in house if x[1] == max_h]
left = min(x[0] for x in max_pillars)
right = max(x[0] for x in max_pillars)
area += (right - left + 1) * max_h


print(area)
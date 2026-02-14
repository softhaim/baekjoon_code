'''
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.

만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
(1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.
'''

import sys

input = sys.stdin.readline

N = int(input())

map_arr = []

count_0 = 0
count_1 = 0
count_minus1 = 0

for i in range(N):
    map_arr.append(list(map(int, input().split())))

'''
x,y부터 시작해서 첫원소부터 현재 분할해둔 영역 전체가 같은 원소인지 체크하는 함수
'''
def is_uniform(x,y,size):
    first = map_arr[x][y]

    for i in range(x,x+size):
        row = map_arr[i]
        for j in range(y,y+size):
            if row[j] != first:
                return False, None
    return True, first

'''
분할하는 함수. -1,0,1 기점으로 전부 ok면 해당 +1 하고 아니라면 분할함 9개 영역으로
'''
def divide(x,y,size):
    global count_0, count_1, count_minus1
    ok, value = is_uniform(x,y,size)

    if ok:
        if value == 0:
            count_0 += 1
        elif value == 1:
            count_1 += 1
        else: # 2
            count_minus1 += 1
    else: # not ok
        '''
        size 만큼 해서 나눠서 정복
        '''
        div_size = size//3
        divide(x,y,div_size) # 맨 왼쪽 위 부터 1번
        divide(x,y+div_size,div_size) # 2
        divide(x,y+(div_size*2),div_size) # 3
        divide(x+div_size,y,div_size) # 4
        divide(x+div_size,y+div_size,div_size) # 5
        divide(x+div_size,y+(div_size*2),div_size) # 6
        divide(x+(div_size*2),y,div_size) # 7
        divide(x+(div_size*2),y+div_size,div_size) # 8
        divide(x+(div_size*2),y+(div_size*2),div_size) # 9
    return

divide(0,0,N)
print(count_minus1)
print(count_0)
print(count_1)

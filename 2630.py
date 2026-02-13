'''
색종이를 분할정복으로 잘라나가면서 전체가 1이거나 0 인경우까지 잘라나가고 왼위 부터 오아래까지 순서로 해서 1,2,3,4 구성 
'''

import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

white = 0
blue = 0

'''
해당 분할 한 영역이 한 원소로만 차있는지 검사하는 함수
'''
def is_uniform(x, y, size):
    # x,y에서 시작해서 size 까지의 원소가 전부 같은지 검사하는 함수
    first = arr[x][y]
    for i in range(x,x+size):
        row = arr[i]
        for j in range(y, y+size):
            if row[j] != first: # 처음 값과 다르면 해당 색으로 전부 결국 칠해진것이 아니기에 false 반환
                return False, None
    return True, first

'''
여기서는 분할해서 각각의 사분면을 잘라서 찾는 함수.
'''
def divide_map(x, y, size):
    global white, blue

    mid = size // 2

    ok, value = is_uniform(x,y, size)
    
    if ok:
        if value == 0: # white 경우
            white += 1
        else: # blue 경우
            blue += 1
        return 
    else: # 한 원소로 차있는게 아니기에 분할해서 다시 s찾을 것임
        divide_map(x,y, mid) # 1번 사분면
        divide_map(x,y+mid, mid) # 2번 사분면
        divide_map(x+mid,y, mid) # 3번 사분면
        divide_map(x+mid,y+mid, mid) # 4번 사분면 


divide_map(0,0,N)
print(white)
print(blue)
'''
백트랙킹 문제. 스도쿠 문제이고, 값을 하나씩 넣어서 0인 부분에서 해당하는 값을 넣었을 때, 되는 지 체크하고 되면 넣으면서 모든 0 대해서 다 넣어서 되었다면 출력하고 종료하도록 함.
'''
import sys

input = sys.stdin.readline

def check(x, y, num):
    # 행 검사
    for i in range(9):
        if arr[x][i] == num:
            return False
    
    # 열 검사
    for i in range(9):
        if arr[i][y] == num:
            return False
    
    # 3x3 검사
    # start_x = ((x - 1) // 3) * 3 + 1
    # start_y = (y // 3) * 3
    if x<=2:
        start_x = 0
    elif 3<=x<=5:
        start_x = 3
    else:
        start_x = 6
    
    if y<=2:
        start_y = 0
    elif 3<=y<=5:
        start_y = 3
    else:
        start_y = 6

    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if arr[i][j] == num:
                return False

    return True

def dfs(idx):
    if idx == len(idx_0):
        for idx, row in enumerate(arr):
            print(*row)
        exit(0)
    
    x, y = idx_0[idx]

    for num in range(1,10):
        if check(x,y, num):
            arr[x][y] = num
            dfs(idx+1)
            arr[x][y] = 0

if __name__ == "__main__":
    arr = []
    idx_0 = []
    for i in range(9):
        input_row = list(map(int, input().split()))
        for idx, val in enumerate(input_row):
            if val == 0:
                idx_0.append((i,idx))
        arr.append(input_row)
    dfs(0)

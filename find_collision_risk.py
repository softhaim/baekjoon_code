'''
r 좌표가 먼저 변해야 하기에 routes 에서 i,j 에서 j 의 x 좌표에 맞추어서 먼저 이동해야함.

시간 t 일때 지나는 것들 좌표 count 하는거 만들고 이게 2 이상인거 있으면 각각 answer += 1
'''
from collections import defaultdict

def solution(points, routes):
    time_table = defaultdict(lambda: defaultdict(int)) # 새 키가 나오면 int dict 만들도록
    
    for route in routes:
        # 시작 위치도 시간 0에 기록
        time = 0
        start = route[0]
        x, y = points[start - 1]
        time_table[time][(x, y)] += 1
        
        for i, j in zip(route, route[1:]):
            i_x, i_y = points[i-1] 
            j_x, j_y = points[j-1]
            
            while j_x != i_x:
                if j_x > i_x:
                    i_x += 1
                else:
                    i_x -= 1
                time += 1
                time_table[time][(i_x,i_y)] += 1
            
            while j_y != i_y:
                if j_y > i_y:
                    i_y += 1
                else:
                    i_y -= 1
                time += 1
                time_table[time][(i_x,i_y)] += 1
    
    count = 0

    # 1. 각 시간대별 내부 딕셔너리를 하나씩 가져옴
    for sub_dict in time_table.values():
        # 2. 내부 딕셔너리에 저장된 튜플 키의 카운트(값)들을 확인
        for value in sub_dict.values():
            if value > 1:
                count += 1
    return count

if __name__ == "__main__":
    print(f"{solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]])}, Gold ANS: 1")
    print(f"{solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]])}, Gold ANS: 9")
    print(f"{solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]],	[[2, 3, 4, 5], [1, 3, 4, 5]])}, Gold ANS: 0")
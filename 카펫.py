def solution(brown, yellow):

    for w in range(yellow, 0, -1):
        if yellow % w == 0: # 나누어 떨어지면 -> 해당 길이 가로길이로 가능
            h = yellow//w
            if brown == (w+2)*(h+2)-yellow: # 해당 가로 세로 길이로 감쌀 수 있는지 확인
                return [w+2,h+2]

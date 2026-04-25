'''
문제 설명
명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다. 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다. 이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.

아래 표는 4가지 명함의 가로 길이와 세로 길이를 나타냅니다.

명함 번호	가로 길이	세로 길이
1	60	50
2	30	70
3	60	30
4	80	40
가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑을 만들면 모든 명함들을 수납할 수 있습니다. 하지만 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다. 이때의 지갑 크기는 4000(=80 x 50)입니다.

모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

제한사항
sizes의 길이는 1 이상 10,000 이하입니다.
sizes의 원소는 [w, h] 형식입니다.
w는 명함의 가로 길이를 나타냅니다.
h는 명함의 세로 길이를 나타냅니다.
w와 h는 1 이상 1,000 이하인 자연수입니다.
입출력 예
sizes	result
[[60, 50], [30, 70], [60, 30], [80, 40]]	4000
[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	120
[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	133
'''

import sys
input = sys.stdin.readline

def solution(sizes):
    max_x = 0
    max_y = 0
    for val in sizes:
        x, y = val
        if x < y:
            x, y = y, x
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    answer = max_x * max_y
    # return max(max(x) for x in sizes) * max(min(x) for x in sizes) # 이렇게도 할 수 있는거 같지만, 이는 2n 이라서 위보단 좀 시간 걸릴듯. 
    # rotated = [(max(w, h), min(w, h)) for w, h in sizes] # 이렇게 비열 만들고 하면 2줄컷이나, 이것도 배열을 만들기에 공간 복잡도 상 그냥 위 코드가 좀 길어도 나을듯.
    return answer

if __name__ == "__main__":
    sizes = list()
    while true:
        try:
            sizes.append(list(map(int,input().split())))
        except:
            print(solution(sizes))
            break

'''
문제 설명
x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인 서로 다른 크기의 원이 두 개 주어집니다. 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때, 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를 return하도록 solution 함수를 완성해주세요.
※ 각 원 위의 점도 포함하여 셉니다.

제한 사항
1 ≤ r1 < r2 ≤ 1,000,000
입출력 예
r1	r2	result
2	3	20

x 좌표로 반지름 만큼만 돌면서 사실상 사분면 하나에서의 점 개수를 구함. 그러고 *4
'''

import math

def solution(r1, r2):
    answer = 0
    for i in range(1, r2+1):
        j2 = math.floor(math.sqrt(r2**2 - i**2))
        # x가 r1보다 크면 안쪽 원을 벗어났으므로 최소 y는 0.
        if i < r1:
            j1 = math.ceil(math.sqrt(r1**2 - i**2))
        else:
            j1 = 0
        
        answer += (j2 - j1 +1)*4 # +1 의 이유는 해당 점도 포함이기에, *4 는 좌우상하 대칭으로 이만큼 점이 있으니까
        
    return answer
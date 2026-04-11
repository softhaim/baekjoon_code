'''
가로수들이 모두 같은 간격이 되도록 가로수를 추가로 심는 사업을 추진하고 있다. KOI 시에서는 예산문제로 가능한 한 가장 적은 수의 나무를 심고 싶다.

편의상 가로수의 위치는 기준점으로 부터 떨어져 있는 거리로 표현되며, 가로수의 위치는 모두 양의 정수이다.

예를 들어, 가로수가 (1, 3, 7, 13)의 위치에 있다면 (5, 9, 11)의 위치에 가로수를 더 심으면 모든 가로수들의 간격이 같게 된다. 또한, 가로수가 (2, 6, 12, 18)에 있다면 (4, 8, 10, 14, 16)에 가로수를 더 심어야 한다.

심어져 있는 가로수의 위치가 주어질 때, 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 구하는 프로그램을 작성

우선 가로수들 간격을 구해서 리스트에 넣어두고 이 값들의 최대공약수를 찾으면 그 간격으로 몇개 넣어야하는지 찾으면 되지 않을까 싶음. 
'''

import math, sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    input_num = []
    for _ in range(N):
        input_num.append(int(input()))
    diff_list = []
    for i in range(1,N):
        diff_list.append(input_num[i] - input_num[i-1])
    gcd_result = math.gcd(*diff_list)
    
    # val = input_num[0]
    # i = 1
    # result = 0
    # while val <= input_num[-1] and i < N:
    #     if val + gcd_result != input_num[i]: # 다음 간격에 심어야 함
    #         result += 1
    #         val = val + gcd_result
    #     else:
    #         val = input_num[i]
    #         i += 1
    # 위처럼 할 수도 있지만, 사이 거리 diff가 있고 공통 간격이 g라면, 그 사이 간격을 diff//g 했을때 1 이여야 공통간격인거고 1 이상이라면 diff//g-1한 개수 만큼 더 심어야 하는것
    # 위처럼 해도 정답이나, 시간 차이가 위처럼 하면 3268ms, 아래처럼 하면 140ms 이다.
    result = 0
    for d in diff_list:
        result += d // gcd_result - 1
    print(result)
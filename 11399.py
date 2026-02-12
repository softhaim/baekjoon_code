'''
줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.
'''

import sys

input = sys.stdin.readline

N = int(input())

p_i = list(map(int, input().split()))

p_i.sort()

sum_pi = 0
sum_arr = []
for i in range(1, N+1):
    sum_pi = sum_pi + p_i[i-1]
    sum_arr.append(sum_pi)
print(sum(sum_arr))
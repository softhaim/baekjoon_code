'''
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

동전 개수 구하는 문제는 그리디로 해서 가장 큰 수 부터 해서 남은 나머지를 가지고 계속 카운트를 세는것임. 

'''

import sys

input = sys.stdin.readline


N, K = map(int, input().split())
a_i = []
for i in range(N):
    a_i.append(int(input()))

mod_val = K
cnt = 0

for i in range(N-1,-1, -1):
    if a_i[i] > K:
        continue
    elif a_i[i] <= K and mod_val >= a_i[i]:
        # 여기서는 현재 값이 K보다 작으니까 나눈 나머지 값 구해둬야함.
        # print(f'mod_val//a_i[i] = {mod_val//a_i[i]}')
        cnt += mod_val//a_i[i]
        mod_val = mod_val%a_i[i]

    elif mod_val == 0:
        break

print(cnt)
'''
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성
'''

import re
import sys

input = sys.stdin.readline

s = input()

nums = list(map(int, re.findall(r'[+-]?\d+', s)))
# print(nums)  # [55, -50, 40] 이런 식으로 저장 됨.

'''
가장 작은 수로 만들려면 음수인거 나오고 나서 그 이후의 + 값들을 괄호로 묶는다 생각하고 음수로 빼주면 됨.
'''
change_minus = False
sum_nums = []
for i in range(len(nums)):
    if change_minus == False and nums[i] < 0 :
        change_minus = True
        sum_nums.append(nums[i])
    elif change_minus and nums[i] >     0 : # 양수인데 변경해야 하는 경우 앞에서 음수 나와서 바꿀경우
        sum_nums.append(-nums[i])
    else: # 남은 경우의 수는 false 에 양수 경우랑 기존에 마이너스 있어서 변경 중이였는데 음수 나온 경우 인데 이 경우는 그냥 넣어줌
        sum_nums.append(nums[i])

print(sum(sum_nums))
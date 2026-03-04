'''
산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성.
정렬하고 투포인터로 left right 두고 적절하게 올리고 내라다가 찾으면 그 left, right 출력.
'''

import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N-1
min_ans = float('inf')
result = None
while left < right:
    s = arr[left] + arr[right]
    min_temp = min(abs(min_ans), abs(s))
    if min_temp == 0:
        result = (left, right)
        break
    elif min_temp == abs(s):
        if s < 0: min_ans = -(min_temp)
        else: min_ans = min_temp
        result = (left, right)
    if s < 0:
        left += 1
    elif s > 0:
        right -= 1
print(arr[result[0]], arr[result[1]])
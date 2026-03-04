'''
투 포인터 문제. 앞 뒤 기준으로 두고 이 합이 목표보다 작으면 작은값인 왼쪽 포인터를 늘리고, 크면 큰 값인 오른쪽 포인터 위치를 줄임.
'''

import sys

input = sys.stdin.readline

n = int(input())

input_arr = list(map(int, input().split()))
input_arr.sort()

x = int(input())

cnt = 0
left = 0
right = n - 1
cnt = 0

while left < right:
    s = input_arr[left] + input_arr[right]

    if s == x:
        cnt += 1
        left += 1
        right -= 1
    elif s < x:
        left += 1
    else:
        right -= 1
print(cnt)
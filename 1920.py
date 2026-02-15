'''

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.


'''

import sys

input = sys.stdin.readline


'''

첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

'''

N = int(input())

arr = list(map(int, input().split()))

M = int(input())

M_list = list(map(int, input().split()))

'''
arr 를 sort 하고 그 다음 여기서 binary search 하는 문제인듯
'''

arr.sort()

def binary_search(find_val):
    start = 0
    end = N-1
    mid = (start+ end) // 2
    while (mid >= start and mid <= end):
        if find_val == arr[mid]:
            return 1
        elif arr[mid] < find_val: 
            start = mid +1 
        elif arr[mid] > find_val:
            end = mid -1
        mid = (start+ end) // 2
    return 0

for val in M_list:
    is_find = binary_search(val)
    print(is_find)
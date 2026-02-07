#20922

'''
같은 원소가 
$K$개 이하로 들어 있는 최장 연속 부분 수열의 길이 구함 -> 최장 연속 부분 수열 길이 구하는 문제

투 포인터 문제로, 아래와 같이 풀 수 있다.

list의 최대값만큼의 길이를 가진 배열을 생성한다. (sequence 배열 생성)
투포인터를 위해 left, right 변수를 생성하고 right가 arr 길이에 도달할 때까지 loop를 돈다.
sequence 배열에서 해당 idx값이 M(중복횟수) 보다 작으면 값을 1 추가하고 right를 전진시킨다.
조건에 만족하지 않으면 left idx 값을 1 빼주고, left를 전진시킨다.
결과값 변수에 수열의 길이를 할당한다.
출력 끝
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sequence = [0]* (max(arr) + 1) # arr 최대 값 만큼 길이 가진 배열 생성
left, right = 0, 0
result = 0

# N 만큼 loop 
while(right < n):
    # 배열에서 해당 idx값의 count 를 세고, 이값이 M 보다 작으면 더함. M 이상이면 이것이 M 번 이상 중복해서 나온것이니 
    if sequence[arr[right]] < m:
        sequence[arr[right]] += 1
        right += 1
    # 아니면 M 번 이상 중복이니까 이것 부터는 최장 수열 계산이 안될것. 왼쪽꺼를 빼고 그값은 빠지니 카운트 내림. 
    # 이것이 left 가 겹치는 값이 나올때까지 반복할 것임. 
    # right 는 + 안되는 상황에서 arr[right]가 지금 = m 인 상황이기에 이 m 값을 저 left 쪽이 가면서 빼줘야만 이후 값이 비교 될것임.
    else: 
        sequence[arr[left]] -= 1
        left += 1
    # 수열 길이 현재 최고 값과, right-left 한 값 비교해서 큰 값으로 갱신하며 할당. 
    result = max(result, right-left)

print (result)
'''
가장 무거운 사람 + 가장 가벼운 사람 <= limit 이면 태우고 아니면 따로 버림
'''
import math

def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else:
            right -= 1
            answer += 1
    return answer

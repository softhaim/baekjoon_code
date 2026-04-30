'''
1번째 자리 가중치 = 1 + 5 + 25 + 125 + 625 = 781
2번째 자리 가중치 = 1 + 5 + 25 + 125 = 156
3번째 자리 가중치 = 1 + 5 + 25 = 31
4번째 자리 가중치 = 1 + 5 = 6
5번째 자리 가중치 = 1
'''
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]

    answer = 0

    for i, ch in enumerate(word):
        answer += vowels.index(ch) * weights[i] + 1

    return answer

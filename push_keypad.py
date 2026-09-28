'''
문제 설명
스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.

kakao_phone1.png

이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

[제한사항]
numbers 배열의 크기는 1 이상 1,000 이하입니다.
numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
hand는 "left" 또는 "right" 입니다.
"left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.

입출력 예
numbers	hand	result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"
'''
from collections import defaultdict

def solution(numbers, hand):
    answer = ""
    dp = defaultdict(tuple)
    dp[0] = (3,1)
    
    for i in range(1,10):
        dp[i] = (((i-1)//3),(i-1)%3)
    
    now_l = (3,0)
    now_r = (3,2)
    
    for num in numbers:
        move_i, move_j = dp[num][0], dp[num][1]
        if move_j == 0: # 1,4,7
            answer += "L"
            now_l = dp[num]
        elif move_j == 2: # 3,6,9
            answer += "R"
            now_r = dp[num]
        else: # 2, 5, 8, 0
            l_d = abs(now_l[0] - move_i) + abs(now_l[1] - move_j)
            r_d = abs(now_r[0] - move_i) + abs(now_r[1] - move_j)

            # 방향 결정
            move = "L" if l_d < r_d or (l_d == r_d and hand == "left") else "R"
            
            answer += move
            if move == "L":
                now_l = dp[num]
            else:
                now_r = dp[num]
        
    return answer

if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    ans = solution(numbers, hand)
    print(f"Input: {numbers}, {hand}, Output: {ans}, is_correct: {ans == 'LRLLLRLLRRL'}")  # Output: "LRLLLRLLRRL"
    
    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = "left"
    ans = solution(numbers, hand)
    print(f"Input: {numbers}, {hand}, Output: {ans}, is_correct: {ans == 'LRLLRRLLLRR'}")  # Output: "LRLLRRLLLRR"
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = "right"
    ans = solution(numbers, hand)
    print(f"Input: {numbers}, {hand}, Output: {ans}, is_correct: {ans == 'LLRLLRLLRL'}")  # Output: "LLRLLRLLRL"
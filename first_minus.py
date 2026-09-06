'''
문제 설명
정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.

제한사항
5 ≤ num_list의 길이 ≤ 100
-10 ≤ num_list의 원소 ≤ 100

입출력 예
num_list	result
[12, 4, 15, 46, 38, -2, 15]	5
[13, 22, 53, 24, 15, 6]	-1
'''
def solution(num_list):
    for idx, val in enumerate(num_list):
        if val < 0:
            return idx
    
    return -1

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([12, 4, 15, 46, 38, -2, 15], 5),
        ([13, 22, 53, 24, 15, 6], -1),
        ([-1, 2, 3], 0),
        ([1, 2, 3], -1),
        ([0, -5, 10], 1)
    ]

    for i, (num_list, expected) in enumerate(test_cases):
        result = solution(num_list)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
    
    print("All test cases passed!")
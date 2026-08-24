'''
문제 설명
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

제한사항
3 ≤ n ≤ 1,000,000

입출력 예
n	result
10	3
12	11

'''
def solution(n):
    answer = 0
    num = 2
    while num < n:
        if (n-1) % num != 0:
            num += 1
            continue
        answer = num
        break
    
    return answer

if __name__ == "__main__":
    n = 10
    answer = solution(n)
    print(f"solution({n}) = {answer}, is_correct={answer == 3}")  # Output: 3

    n = 12
    answer = solution(n)
    print(f"solution({n}) = {answer}, is_correct={answer == 11}")  # Output: 11
'''
문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000
입출력 예
left	right	result
13	17	43
24	27	52

'''

# 수학적으로 모든 자연수의 약수의 개수는 무조건 짝수개. 오직 제곱수만 예외적으로 약수의 개수가 홀수개가 되기에 제곱수만 찾는 풀이 방법
def solution1(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

'''
우리가 구하고 싶은 범위가 A = 13부터라 하면
예를 들어 2의 배수를 찾고 싶다 할 때,
13은 2의 배수 아니고 14가 배수임.
그렇다면 14부터 시작하면서 + 2씩 되면서 순회하며 +1 count 해주면 되는거임.
이를 위해서 {(13//2)+1} * 2 해서 left 의 나눈 몫 보다 1 큰수에 현재 i 를 곱해서 left 시작으로부터 현재 i 의 배수 시작 지점 구함.

예를 들어 3의 배수를 찾고 싶다 할 때,
13, 14도 3의 배수가 아니고, 15가 13 이상이면서 가장 처음 만나는 3의 배수. 
즉, 우리가 원하는 결과(start)는 15가 나와야 함 이렇게 효율적으로 배수 부분에 대해서 cnt 저장.
'''

def count_divisors_range(A, B):
    # A부터 B까지의 약수 개수를 저장할 배열 (인덱스 0이 숫자 A를 의미)
    size = B - A + 1
    counts = [0] * size
    
    # 1부터 B까지의 숫자가 구간 [A, B] 내에 가지는 배수를 찾아 카운트
    for i in range(1, B + 1):
        # A가 i로 딱 나누어떨어지면 시작값은 그냥 A
        if A % i == 0:
            start = A
        # 나누어떨어지지 않으면, 다음 배수로 넘어가야 함
        else:
            start = (A // i + 1) * i

        # 구간 내의 i의 배수들을 돌며 1씩 누적
        for j in range(start, B + 1, i):
            counts[j - A] += 1
            
    return counts

def solution(left, right):
    answer = 0
    cnt_arr = count_divisors_range(left, right)
    print(cnt_arr)
    # 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수 구하기
    for idx, val in enumerate(cnt_arr):
        if val % 2 == 0:
            answer += idx+left
        else:
            answer -= idx+left
            
    return answer

if __name__ == "__main__":
    left = 13
    right = 17
    ans = solution(left, right)
    print(f"solution({left}, {right}): {ans} is_correct: {ans == 43}")  # Output: 43

    left = 24
    right = 27
    ans = solution(left, right)
    print(f"solution({left}, {right}): {ans} is_correct: {ans == 52}")  # Output: 52
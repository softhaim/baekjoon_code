'''
문제 설명
철호는 수열을 가지고 놀기 좋아합니다. 어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다. 원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다. 예를 들어 수열 [7, 9, 1, 1, 4] 로 원형 수열을 만들면 다음과 같습니다.
그림.png
원형 수열은 처음과 끝이 연결되어 끊기는 부분이 없기 때문에 연속하는 부분 수열도 일반적인 수열보다 많아집니다.
원형 수열의 모든 원소 elements가 순서대로 주어질 때, 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
3 ≤ elements의 길이 ≤ 1,000
1 ≤ elements의 원소 ≤ 1,000

입출력 예
elements	result
[7,9,1,1,4]	18
'''

def solution(elements):
    # 슬라이딩 윈도우처럼 해서 해당 위치부터 원하는 길이까지의 합을 차례로 구하고 이를 set에 넣어 중복 제거 후 길이 반환
    n = len(elements)
    extended = elements + elements
    result = set()
    
    for i in range(n):
        current_sum = 0
        for j in range(n):
            current_sum += extended[i + j]
            result.add(current_sum)
    
    return len(result)

if __name__ == "__main__":
    elements1 = [7, 9, 1, 1, 4]
    ans1 = solution(elements1)
    print(f"elements:{elements1}, Answer:{ans1}, is_Correct:{ans1 == 18}")
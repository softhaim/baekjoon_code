'''
문제 설명
길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

제한사항
a, b의 길이는 1 이상 1,000 이하입니다.
a, b의 모든 수는 -1,000 이상 1,000 이하입니다.

입출력 예
a	b	result
[1,2,3,4]	[-3,-1,0,2]	3
[-1,0,1]	[1,0,-1]	-2
'''
def solution(a, b):
    answer = 0
    n = len(a)
    for i in range(n):
        answer += a[i]*b[i]
        
    return answer

if __name__ == "__main__":
    io = [
        ([1,2,3,4], [-3,-1,0,2], 3),
        ([-1,0,1], [1,0,-1], -2),
    ]
    ans = [solution(i[0], i[1]) for i in io]
    for i in io:
        print(f"Input: {i[0]}, {i[1]}, Expected: {i[2]}, Got: {ans[io.index(i)]}")
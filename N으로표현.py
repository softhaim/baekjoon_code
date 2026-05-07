'''
문제 설명
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.
입출력 예
N	number	return
5	12	4
2	11	3


n을 가지고 사칙연산으로 만들 수 있는 경우의 수 체크하고 그걸 dp에 저장해둚. -> 만들 수 있는 값에서 number 나오면 return
dp[1] = {5}
dp[2] = {55, 5+5, 5-5, 5*5, 5//5}
      = {55, 10, 0, 25, 1}
dp[3] = {dp[1]과 dp[2] 조합, dp[2]와 dp[1] 조합, 555}
dp[4] = {dp[1]과 dp[3], dp[2]과dp[2], dp[3]과dp[1], 5555}
... 이렇게 8까지 하고 없으면 return -1

'''
def solution(N, number):
    dp = [set() for _ in range(9)] # 최솟값 8보다 크면 -1 임
    
    for i in range(1,9):
        dp[i].add(int(str(N) * (i)))
        
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b != 0: # 0 나누면 안됨
                        dp[i].add(a//b) # 나머지 무시
        if number in dp[i]:
            return i
    return -1

if __name__ == "__main__":
    print(f"{solution(5, 12)}, gold: 4")
    print(f"{solution(2, 11)}, gold: 3")
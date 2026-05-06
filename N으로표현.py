'''
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

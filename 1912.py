'''
n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.
'''

'''
현재 숫자를 포함해서 쭉 숫자를 앞에서부터 더해온 값과 현재 숫자 비교 시 
현재 숫자가 크다면 앞에서 더해온 값은 의미 없음. 총합을 키우는 데 기여할 수 없기 때문이다.
'''
import sys 

input = sys.stdin.readline

n = int(input())
input_num = list(map(int, input().split()))
dp = [0]*n
dp[0] = input_num[0]

for i in range(1,n):
    dp[i] = max(input_num[i], input_num[i]+dp[i-1])


print(max(dp))

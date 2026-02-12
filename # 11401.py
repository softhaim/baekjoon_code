# 11401

import sys

N, K = map(int, sys.stdin.readline().split())

def power(n, k):
    if k == 1:
        return n
    else:
        tmp = power(n, k//2)
        if k % 2 == 0:
            return tmp*tmp % 1000000007
        else:
            return tmp*tmp*n%1000000007

def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % 1000000007
    return n

def binomial_coe(n, k):
    res = factorial(n)/(factorial(k)*factorial(n-k))
    return res % 1000000007

A = factorial(N)
B = (factorial(N-K) * factorial(K)) % 1000000007

# (A/B) % p
# = A * B^-1 % p
# = A * B^-1 * B^p-1 % p
# = A * B^p-2 % p
# = (A % p) * (B^p-2 % p) % p
print((A % 1000000007) * (power(B, 1000000007-2) % 1000000007) % 1000000007 )

'''
하는 이유? (feat. AI (e.g. gemini))
1. 큰 정수 나눗셈 (Long Division / Fast Division)
방식: 초등학교 때 배운 세로셈(Long Division) 방식을 확장하여 큰 수 나눗셈을 수행합니다. 혹은 Newton's method를 활용한 근사 나눗셈을 사용합니다.
복잡도: 피제수(나뉠 수)의 자릿수를 
이라 할 때, O(N^2)
 또는 고속 곱셈 알고리즘(Karatsuba, FFT)을 활용하면 
 ~ O(NlogN)
 수준으로 줄일 수 있습니다.
특징: 숫자가 매우 커지면 연산 횟수가 급격히 증가합니다. 

2. 분할정복 지수 계산 (Exponentiation by Squaring)
방식: 
A^B 를 계산할 때, 
가 짝수이면 (A^(B/2))^2
, 홀수이면 지수에 하나 +1
로 나누어 처리합니다.
복잡도: 지수 
에 대한 로그 시간 복잡도를 가집니다. 즉, O(logB)
입니다.
특징: 지수가 10^18
처럼 엄청나게 커져도, 연산은 60번 정도면 끝나기 때문에 매우 효율적입니다.
'''
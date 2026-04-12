'''
n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성

어떤 합성수 x가 있으면
x = a * b 꼴로 나눠지는데,

만약 a와 b가 둘 다 sqrt(x)보다 크다면

a * b > x

가 되어버려서 모순임.
-> 2부터 sqrt(x)까지만 나눠보면 됨

그래서 합성수라면 반드시
sqrt(x) 이하의 약수 하나는 존재

1.n이 0 또는 1일경우, 2 출력후 끝.
2.n이 √m 보다 작거나 같은 약수를 가지지 않으면 n 출력후 끝.
3.n이 √m 보다 작거나 같은 약수를 가지면 n+=1 후 2번으로 되돌아가기.

이 문제는 체를 처음에는 쓰는 줄 알았는데 n까지의 모든 소수를 한번에 구하기엔 아닌 것 같았음. n 이상인 첫 소수만 찾으면 되기에 그래서 정수론을 몰라서 찾아보고 풂. 복습 권장
'''

import sys, math

input = sys.stdin.readline

def is_prime(x):
    for i in range(3,int(math.sqrt(x))+1,2):
        if x%i == 0: # 루트 x 이하의 약수가 존재하면 -> 합성수 -> 소수 아님
            return False
    return True

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())

        if N <= 2:
            print(2)
            continue
        elif N % 2 == 0: # 짝수는 어차피 합성수임.
            N += 1
        while not is_prime(N):
            N += 2 # 같은 이유로 짝수는 볼 필요 없으니까 +=2 해서 홀수만 봄
        print(N)
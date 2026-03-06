'''
소수인지 어떻게 알지 했는데 이건 검색해보니 에라토스테네스의 체 라는 것을 사용하면 된다고 한다. 
이 문제는 그래서 아래처럼 풀면 될것이다.
1. N 입력
2. 에라토스테네스의 체로 N 이하 소수 리스트 생성
3. 투포인터로 연속합이 N인 경우의 수 카운트
4. 출력

에라토스테네스의 체라는 것의 핵심 아이디어는 아주 단순:

2는 소수다

그러면 2의 배수는 전부 소수가 아님

다음으로 아직 안 지워진 수 3은 소수다

그러면 3의 배수도 전부 소수가 아님

그 다음 5, 7 ... 이런 식으로 반복

즉, 소수 그 자체를 찾는다기보다, 소수가 아닌 수를 지워 나가는 방식
'''


def get_primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve

if __name__ == "__main__":

    N = int(input())

    is_prime_arr = get_primes(N)
    prime_n = list()
    for idx, val in enumerate(is_prime_arr):
        if val == True:
            prime_n.append(idx)

    left = 0
    cnt = 0
    sum_num = 0

    for right in range(len(prime_n)):
        sum_num += prime_n[right]

        while sum_num >= N:
            if sum_num == N:
                cnt += 1
            sum_num -= prime_n[left]
            left += 1

    print(cnt)
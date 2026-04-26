import math
from itertools import permutations # 순서를 고려해서 뽑는 모든 경우의 수 계산

def sieve(n):
    is_prime = [True]*(n+1)
    is_prime[0], is_prime[1] = False, False # 0과 1은 소수가 아니므로 false로 설정
        
    for i in range(2, int(math.sqrt(n))+1):
        for j in range(i*i, n+1, i):
            is_prime[j] = False
    return is_prime

def solution(numbers):
    answer = 0
    posible_set = set()
    
    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length): # numbers 안에 있는 것을 length 만큼 골라서 뽑는 경우의 수 계산
            num = int(''.join(p))
            posible_set.add(num) # set 에다 저장하면서 중복인거 피하면서 잘 저장

    prime = sieve(max(posible_set))
    
    for val in posible_set:
        if prime[val] == True:
            answer += 1
    
    return answer

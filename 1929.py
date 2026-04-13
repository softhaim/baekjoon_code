'''
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성
-> 범위에 해당하는것을 구하는 것은 에라토스테네스의 체 문제
-> 배수들을 없애서 범위내의 소수를 찾는것임.
'''

import sys, math

input = sys.stdin.readline

def find_prime_num(x):
    arr = [i for i in range(x+1)]
    arr[1] = 0
    for i in range(2,int(math.sqrt(x))+1): # 2부터 x의 제곱근까지의 모든 수를 확인
        for j in range(i*i, x+1, i): # i 의 배수들을 찾음 -> i 자신은 제외. 자기 자신 자체는 소수일 수 있으니.
            arr[j] = 0
    return [i for i in arr[2:] if arr[i]]

if __name__ == "__main__":
    M, N = map(int, input().split())
    prime_arr = find_prime_num(N)

    for val in prime_arr:
        if val >= M:
            print(val)
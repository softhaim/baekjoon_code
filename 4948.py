
'''
자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성
1 ≤ n ≤ 123,456
123456*2 만큼 해서 에라토스테네스의 체 를 구해둠. 그러고 나서 범위 내의 소수개수 몇개인지 cnt 하면 됨.
'''

import sys, math

input = sys.stdin.readline

def find_prime_num(x):
    for i in range(2, int(math.sqrt(x))+1):
        for j in range(i*i, x+1, i):
            arr[j] = 0
    return [i for i in arr[2:] if arr[i]]

if __name__ == "__main__":
    arr = [i for i in range(123456*2 + 1)]
    arr[1] = 0
    prime_arr = find_prime_num(123456*2)
    while True:
        N = int(input())
        if N == 0: break
        cnt = 0
        for val in prime_arr:
            if N < val <= 2*N:
                cnt += 1
            elif val > 2*N:
                break
        print(cnt)
'''
골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자

처음 든 생각 -> 입력 최대까지의 체를 한번구하고 입력된 수와 가까운 소수를 bisect_left로 찾고 인덱스 수부터 해서 해당 소수에서 찾고자 하는 수를 뺀 값 만큼의 수가 소수인지 또 bisect해서 찾음.
그 값이 찾는 수랑 같으면 있는거니까 cnt+1 하고 아님 말고

근데 체를 구할때 그냥 arr 로 반환 하면, bisect 안해도 된다는것을 깨달음. 그 수가 arr 내에서 소수인지 바로 알 수 있으니까.
'''

import sys, math

input = sys.stdin.readline

def make_prime_num(x):
    arr = [ True for _ in range(x+1)]
    arr[1] = False

    for i in range(2,int(math.sqrt(x))+1):
        for j in range(i*i, x+1, i):
            arr[j] = False
    return arr

if __name__ == "__main__":
    T = int(input())    
    prime_arr = make_prime_num(1000000)
    for t in range(T):  
        cnt = 0
        N = int(input())

        for i in range(2, N//2+1):
            if prime_arr[i] and prime_arr[N-i] == True: # 현재 수와 찾고자 하는 수가 소수이면
                cnt += 1
        print(cnt)
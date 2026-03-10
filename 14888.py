'''
입력
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 
둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.

출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 
연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 
또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

*주의*
또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.

이 문제는 백트랙킹으로 차례대로 연산자 넣고 해보고 완성해서 최대 최소 저장 한 뒤에, 다시 다른 연산자일때 해보면서 하는 약간 dfs비슷한 그런 문제.
'''

import sys

input = sys.stdin.readline

def dfs(idx, pre_val):
    global sum_max, sum_min

    for idx_op, op in enumerate(a_i):
        if op != 0:
            a_i[idx_op] -= 1
            if idx_op == 0:
                now_val = pre_val+arr[idx]
            elif idx_op == 1:
                now_val = pre_val-arr[idx]
            elif idx_op == 2:
                now_val = pre_val*arr[idx]
            else: # 문제에서 정수 나눗셈으로 몫을 취한다 명시 됨. 
                if pre_val < 0:
                    now_val = -(-pre_val//arr[idx])
                else:
                    now_val = pre_val//arr[idx] 
            if idx == len(arr)-1:
                sum_max = max(sum_max, now_val)
                sum_min = min(sum_min, now_val)
                

            dfs(idx+1, now_val)
            a_i[idx_op] += 1

if __name__ == "__main__":

    N = int(input())
    
    arr = list(map(int, input().split()))

    a_i = list(map(int, input().split()))
    sum_max = -float('inf') # 처음엔 0으로 했는데 0보다 작을 수 있어서 바꿈
    sum_min = float('inf')

    dfs(1,arr[0])

    print(sum_max)
    print(sum_min)
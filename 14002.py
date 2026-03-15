'''
증가하는 부분수열 구하는 것
'''

import sys
from bisect import bisect_left

input = sys.stdin.readline
'''
2,4,6,8 가 최장 이라 할때, 이후 1, 2 들어오면 tails는 1,2, 를 받아서 1,2,6,8이 될 것이다. 
하지만 기존 tails는 이래도 길이 자체는 아까 2,4,6,8일때 최대였고 이 길이가 4였고 그 값은 6, 8이 남아서 길이는 기록된다.
근데, 이를 출력 할때 원소단위는 문제가 생기니, 이를 prev에 기록을 해둠. 단순 값으로 저장하면 문제가 생기니 (2일때 끝인데 아까 1로 인해 1도 나올 수 있으니) 입력 배열에서의 idx로 기록 함.
그래서 8이 이전값은 6, 6은 넣을때는 4였고, 4는 2였다. 2는 최장 수열 시작이라서 값이 초기화된 값 그대로 일거니 -1 로 초기화 해두고 -1 이라면 수열 종료.
'''
def lis():
    tails = []
    tails_idx = []
    prev = [-1] * N 

    for i, x in enumerate(a_i):
        idx = bisect_left(tails, x)

        if idx == len(tails):
            tails.append(x)
            tails_idx.append(i)
        else:
            tails[idx] = x
            tails_idx[idx] = i

        if idx > 0: # 현재 삽인하려는 위치 전의 idx가 무엇인지를 기록. 만약 0번째 idx 라면 그 경우 최장 수열이 끝나고 새롭게 기록을 하는 것일 거임. 이전 값이 없으니 저장 안함.
            prev[i] = tails_idx[idx - 1]

    lis = []
    cur = tails_idx[-1]
    while cur != -1:
        lis.append(a_i[cur])
        cur = prev[cur]

    lis.reverse()
    return len(lis), lis

if __name__ == "__main__":
    N = int(input())
    a_i = list(map(int, input().split()))

    result_len, result_arr = lis()
    print(result_len)
    print(*result_arr)
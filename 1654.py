'''
집에서 시간을 보내던 오영식은 박성원의 부름을 받고 급히 달려왔다. 박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.

이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다. 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 
예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)

편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 
그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

'''

'''
문제를 보아하나, 이분 탐색으로 저 각각에 대해서 순회하면서 현재의 값으로 잘랐을때 나오는 개수가 11개가 나오는지를 구하는것일듯

예를 들어서 처음에는 우선 가장 큰 랜선을 기준으로 자름
그다음에 이를 반으로 자름.
그렇게 해서 찾고 난 뒤 max 값 저장해두고 mid 랑 start 나 end 랑 같아질때까지 함. 그렇게 했을 때, max 값을 반환. 
그냥 반환하면 8,8 주어질때 4개 만드는덷에서 3을 골랐을때도 4개지만 4로 해도 4개이기에 4를 찾으려면 max까지 잘 찾아야 할것임.

핵심은 위 처럼 max 값을 찾는것이고 이를 위한 분기로 if 문을 count_lan >= find_val 로 같을때를 포함하면서 여기서 max값을 우선 저장해두고, start를 해당 mid+1 로 해서 찾아보면서 max가 더있는지 이분탐색 하도록 함.
만약에 나오면 해당 값으로 max 갱신하는거고 그렇게 찾다가 start <= end 될때까지 찾은거면 전부 찾은거기에 max 반환하고 종료.
'''

import sys

input = sys.stdin.readline

K, N = map(int, input().split())

lan_arr = []
for i in range(K):
    lan_arr.append(int(input()))

def binary_search(find_val):
    start = 1
    end = max(lan_arr) # 여길 min으로 하니까 틀림 반례로 K=2, N=2 10, 100 등어 오면 50으로 2개 자르면 되는데 mind으로 하면 안되기 때문. 
    mid = (start+end) // 2
    max_val = 0
    while (start<= end):
        count_lan = 0
        for val in lan_arr:
            count_lan += val // mid
        if count_lan >= find_val:
            max_val = max(max_val,mid)
            start = mid + 1
        elif count_lan < find_val:
            end = mid -1
        mid = (start+end)//2
    return max_val

print(binary_search(N))
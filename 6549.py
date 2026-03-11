'''
히스토그램에서 가장 큰 직사각형 구하는 문제.
분할 정복으로 풀 수 있다 했는데 감도 안와서 컨닝함.

왼쪽 구간 안에만 있는 경우

오른쪽 구간 안에만 있는 경우

가운데를 가로지르는 경우

이 3경우를 본다. 
시간은 로 308ms 로, 176ms 인 스택 사용 방법보다 느리긴 함 O(nlogn) vs O(n) 차이.
'''

import sys

input = sys.stdin.readline

def solve(left, right, h):
    if left == right:
        return h[left]
    mid = (left + right)//2
    find_max = max(solve(left, mid, h), solve(mid+1,right,h))

    # 여기가 가운데 부분
    lo = mid
    hi = mid+1
    height = min(h[lo],h[hi])
    find_max = max(find_max, height*2)

    while left < lo or hi < right:
        # 오른쪽으로 확장
        if hi < right and (lo == left or h[lo-1]<h[hi+1]): # 현재 오른쪽 탐색 범위가 더있고, 왼쪽은 탐색 끝까지 다 했거나, 오른쪽의 높이가 왼쪽보다 더 클경우, 오른쪽 추가.
            hi += 1
            height = min(height, h[hi]) # 오른족이 더 작으면 그 값으로 갱신.
        # elif left < lo and (right == hi or h[lo-1]>h[hi+1]): -> 이러면 동일 경우에 안되길래 그냥 아래 else로 함.
        else:
            lo -= 1
            height = min(height, h[lo])
        find_max = max(find_max, height*(hi-lo+1)) # 탐색하면서 갱신된 height 으로 길이 계산시, 최댓값 갱신하면 그 값기록. 처음에는 어차피 가장 작은 height 로 갱신하니까 그 값과 비교하고자 하는 범위로 계산하면 되는거 아닌가 했지만, 그 과정속에서 height 가 최종으로 작아지기 전에 max가 갱신된다면 그 값을 기록해줘야하기에 이렇게 해야함.
    
    return find_max


if __name__ == "__main__":
    while True:
        arr = list(map(int, input().split()))
        if arr[0] == 0:
            break
        n = arr[0]
        h = arr[1:]
        print(solve(0, n-1, h))
import sys
from bisect import bisect_left

input = sys.stdin.readline

def lis_lengths_strict(arr):
    """
    각 i에 대해:
      L[i] = arr[i]를 '마지막 원소로' 갖는 (strict) LIS 길이

    핵심 아이디어 (patience sorting):
      tails[t] = 길이가 (t+1)인 증가 부분수열들 중 "마지막 값(꼬리)"의 최솟값
    tails는 항상 오름차순 정렬 상태가 유지되므로,
    매 원소 x에 대해 bisect_left(tails, x)로 들어갈 위치(pos)를 O(log N)에 찾는다.

    strict 증가(<)를 원하므로 bisect_left 사용:
      - 같은 값이 있으면 왼쪽 위치를 주어 '길이 증가'가 발생하지 않게 함
    """
    tails = []               # 길이별 "최소 꼬리값"을 저장하는 배열 (정렬 유지)
    L = [0] * len(arr)       # i에서 끝나는 LIS 길이를 저장

    for i, x in enumerate(arr):
        # pos = tails에서 x를 삽입할 가장 왼쪽 위치
        # 즉, tails[pos-1] < x <= tails[pos]를 만족하는 pos (가능하면)
        pos = bisect_left(tails, x) # 정렬된 리스트에서 “x를 삽입할 가장 왼쪽 위치(인덱스)”를 O(log N)으로 찾아주는 함수

        if pos == len(tails):
            # x가 tails의 모든 값보다 큼 => 가장 긴 수열 뒤에 x를 붙여 길이를 1 늘릴 수 있음
            tails.append(x)
        else:
            # 길이는 늘지 않지만, 길이 (pos+1)짜리 수열의 "꼬리값"을 더 작게(x로) 갱신
            # 꼬리값을 작게 만들면 이후 원소로 더 쉽게 연장될 수 있어 유리함
            tails[pos] = x

        # pos는 0-index 기반 "레벨"
        # pos=0 -> 길이 1, pos=1 -> 길이 2 ...
        # 따라서 i에서 끝나는 LIS 길이 = pos + 1
        L[i] = pos + 1

    return L


# -----------------------------
# Main: Longest Bitonic Subsequence (O(N log N))
# -----------------------------
N = int(input())
A = list(map(int, input().split()))

# 1) inc[i] = i에서 끝나는 LIS 길이 (왼 -> 오)
inc = lis_lengths_strict(A)

# 2) dec[i] = i에서 시작하는 부분수열 길이 (오른쪽 방향)
# 배열을 뒤집어서 LIS를 구한 뒤 다시 매핑한다.

rev_neg = [x for x in reversed(A)]      # 뒤집기
rev_inc = lis_lengths_strict(rev_neg)    # 뒤집힌 배열에서 끝나는 LIS 길이들

# rev_inc[k]는 rev_neg[k]에서 끝나는 LIS 길이
# 원래 인덱스 i에 대응하는 뒤집힌 인덱스는 (N-1-i)
# 따라서 dec[i] = rev_inc[N-1-i]
dec = [0] * N
for i in range(N):
    dec[i] = rev_inc[N - 1 - i]

# 3) 바이토닉: i를 peak(꼭대기)로 잡으면
#      (왼쪽 증가 inc[i]) + (오른쪽 감소 dec[i]) - 1
#    -1 하는 이유: peak 원소 A[i]가 양쪽에 중복으로 포함되기 때문
ans = 0
for i in range(N):
    ans = max(ans, inc[i] + dec[i] - 1)

print(ans)

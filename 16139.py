'''
seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10

출력
0
1
2
1
'''

import sys

input = sys.stdin.readline

string_arr = input().strip()
N = int(input())

prefix = [[0] * (len(string_arr) + 1) for _ in range(26)]

'''
ord('a') == 97

ord('b') == 98

…

ord('z') == 122
'''

for i, ch in enumerate(string_arr, start=1):
    idx = ord(ch) - 97
    for c in range(26): # 알파벳 개수반큼 반복하면서 이전에 세었던 값을 현재 값으로 우선 갱신.
        prefix[c][i] = prefix[c][i - 1]
    prefix[idx][i] += 1 # 현재 알파벳 값을 1 증가시킴.

for i in range(N):
    char, start, end = input().split()
    start = int(start)
    end = int(end)
    print(prefix[ord(char) - 97][end+1] - prefix[ord(char) - 97][start]) # 현재 알파벳 개수 합한값에서 시작 인덱스의 값을 빼주면 그 사이에 있는 알파벳 개수를 구할 수 있다.
# 19941.py 

'''
문제
기다란 벤치 모양의 식탁에 사람들과 햄버거가 아래와 같이 단위 간격으로 놓여 있다. 사람들은 자신의 위치에서 거리가 
$K$ 이하인 햄버거를 먹을 수 있다.

햄버거	사람	햄버거	사람	햄버거	사람	햄버거	햄버거	사람	사람	햄버거	사람
1	2	3	4	5	6	7	8	9	10	11	12
위의 상태에서 
$K = 1$인 경우를 생각해보자. 이 경우 모든 사람은 자신과 인접한 햄버거만 먹을 수 있다. 10번의 위치에 있는 사람은 11번 위치에 있는 햄버거를 먹을 수 있다. 이 경우 다음과 같이 최대 5명의 사람이 햄버거를 먹을 수 있다.

2번 위치에 있는 사람: 1번 위치에 있는 햄버거
4번 위치에 있는 사람: 5번 위치에 있는 햄버거
6번 위치에 있는 사람: 7번 위치에 있는 햄버거
9번 위치에 있는 사람: 8번 위치에 있는 햄버거
10번 위치에 있는 사람: 11번 위치에 있는 햄버거
12번 위치에 있는 사람: 먹을 수 있는 햄버거가 없음
 
$K = 2$인 경우에는 6명 모두가 햄버거를 먹을 수 있다.

2번 위치에 있는 사람: 1번 위치에 있는 햄버거
4번 위치에 있는 사람: 3번 위치에 있는 햄버거
6번 위치에 있는 사람: 5번 위치에 있는 햄버거
9번 위치에 있는 사람: 7번 위치에 있는 햄버거
10번 위치에 있는 사람: 8번 위치에 있는 햄버거
12번 위치에 있는 사람: 11번 위치에 있는 햄버거
식탁의 길이 
$N$, 햄버거를 선택할 수 있는 거리 
$K$, 사람과 햄버거의 위치가 주어졌을 때, 햄버거를 먹을 수 있는 사람의 최대 수를 구하는 프로그램을 작성하시오.

입력
첫 줄에 두 정수 
$N$과 
$K$가 있다. 그리고 다음 줄에 사람과 햄버거의 위치가 문자 P(사람)와 H(햄버거)로 이루어지는 길이 
$N$인 문자열로 주어진다.

출력
첫 줄에 햄버거를 먹을 수 있는 최대 사람 수를 나타낸다.
'''


import sys

from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

hamburger = deque(maxlen=k)
people = deque(maxlen=k)
count = 0

s = input().rstrip()

for i in range(n):
    if s[i] == 'H':
        if len(people) > 0: # 사람이 있는 경우
            people.popleft() # 사람이 햄버거를 먹음
            count += 1
        else: # 사람이 없는 경우
            # 현재 사람이 이전의 사람과 거리가 k 미만만인 경우
            if len(hamburger) > 0 and i - hamburger[0] < k:
                hamburger.append(i)
            elif len(hamburger)> 0 and i - hamburger[0] >= k: # 이전 햄버거는 거리가 k 이상이기에 다음 사람은 못먹음 => 제외해야함
                hamburger.popleft()
                hamburger.append(i)
            else:
                hamburger.append(i)
    else: # 사람인 경우
        if len(hamburger) > 0: # 햄버거가 있는 경우
            hamburger.popleft() # 햄버거를 먹음
            count += 1
        else:
            # 현재 햄버거가 이전의 햄버거와 거리가 k 미만만인 경우
            if len(people) > 0 and i - people[0] < k:
                people.append(i)
            elif len(people) > 0 and i - people[0] >= k: # 이전 사람은 거리가 k 이상이기에 다음 햄버거를 못먹음 => 제외해야함
                people.popleft()
                people.append(i)
            else:
                people.append(i)

print(count)
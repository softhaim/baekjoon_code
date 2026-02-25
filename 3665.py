'''
첫째 줄에는 테스트 케이스의 개수가 주어진다. 테스트 케이스는 100개를 넘지 않는다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

팀의 수 n을 포함하고 있는 한 줄. (2 ≤ n ≤ 500)
n개의 정수 ti를 포함하고 있는 한 줄. (1 ≤ ti ≤ n) ti는 작년에 i등을 한 팀의 번호이다. 1등이 가장 성적이 높은 팀이다. 모든 ti는 서로 다르다.
상대적인 등수가 바뀐 쌍의 수 m (0 ≤ m ≤ 25000)
두 정수 ai와 bi를 포함하고 있는 m줄. (1 ≤ ai < bi ≤ n) 상대적인 등수가 바뀐 두 팀이 주어진다. 같은 쌍이 여러 번 발표되는 경우는 없다.

문제가 좀 헷갈리는데, 입력 (a, b)는 “a가 b보다 앞이다”를 새로 알려주는 입력이 아니라, “작년과 비교해서 a와 b의 상대 순위가 바뀌었다” 는 뜻이라고 한다.
그렇기에 현재 순위와 비교해서 저 입력이 들어오면 작년과 관련해서 반대로 뒤집어야하나봄. 
'''
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    last = list(map(int, input().split()))

    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    # 작년 순위로 그래프 구성
    for i in range(n): # 현재 순위 기준
        for j in range(i + 1, n): # 현재 순위 뒤 순서 순회
            a = last[i]
            b = last[j]
            graph[a][b] = True
            indegree[b] += 1

    # 올해 바뀐 관계 반영
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        if graph[a][b]: 
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

    # 위상정렬
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    # q에는 지금 하나만 들었을 것이다. 가장 첫번째꺼. 다른거는 무조건 순서때문에 뒤에 있어야 하나까. 만약 아니라면 사이클인거고, 2개 이상이면 1등이 2명이란 소리라서 ? 일것이다. 
    result = []
    certain = True
    cycle = False

    for _ in range(n):
        if not q:           # 사이클
            cycle = True
            break
        if len(q) > 1:      # 여러 순서 가능
            certain = False

        now = q.popleft()
        result.append(now)

        for nxt in range(1, n + 1):
            if graph[now][nxt]: # 순회 하면서 true 이면 지금 now를 출력함으로 인해서 제약 하나 줄어드는거니까 -1
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        print(*result)
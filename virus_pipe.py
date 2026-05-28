'''
문제 설명
1번부터 n번까지 번호가 붙은 n개의 배양체를 n-1개의 파이프로 이어 하나의 트리 모양을 만들었습니다. 각 파이프는 A,B,C 3개의 종류 중 하나로 초기에 모든 파이프는 닫혀있습니다.

배양체 중 하나가 바이러스에 감염되어 있습니다. 바이러스에 감염된 배양체는 열린 파이프를 통해 연결된 다른 인접한 배양체를 감염시킵니다.

당신은 종류가 같은 파이프를 한꺼번에 모두 열었다가 닫을 수 있습니다. 단, 한 종류의 파이프를 연 후 다시 닫기 전에 다른 종류의 파이프를 열 수 없습니다. 파이프를 열었다 닫는 행동을 최대 k번 반복해 최대한 많은 배양체에 바이러스를 감염시키려고 합니다.

배양체의 개수를 나타내는 정수 n, 감염된 배양체의 노드 번호를 나타내는 정수 infection, 파이프의 정보를 나타내는 2차원 정수 배열 edges, 최대 행동 수를 나타내는 정수 k가 매개변수로 주어집니다. 최대 k번 파이프를 열었다 닫은 후, 감염된 배양체 개수의 최댓값을 return 하도록 solution 함수를 완성해 주세요.

제한사항
2 ≤ n ≤ 100
1 ≤ infection ≤ n
edges의 길이 = n-1
edges[i]는 [x, y, type]의 형태로 x번 노드의 배양체와 y번 노드의 배양체 사이가 type 종류의 파이프로 연결되어 있음을 의미합니다.
1 ≤ x < y ≤ n
1 ≤ type ≤ 3
1은 A, 2는 B, 3은 C 를 나타냅니다.
1 ≤ k ≤ 10
테스트 케이스 구성 안내
아래는 테스트 케이스 구성을 나타냅니다. 각 그룹 내의 테스트 케이스를 모두 통과하면 해당 그룹에 할당된 점수를 획득할 수 있습니다.

그룹	총점	테스트 케이스 그룹 설명
#1	10%	트리가 일렬 모양입니다. 즉, 각 배양체에 연결된 파이프는 1개 혹은 2개입니다.
#2	20%	파이프의 type은 A 혹은 B만 주어집니다.
#3	30%	한 배양체에 연결된 파이프의 type이 모두 다릅니다.
#4	40%	추가 제한 사항 없음
입출력 예
n	infection	edges	k	result
10	1	[[1, 2, 1], [1, 3, 1], [1, 4, 3], [1, 5, 2], [5, 6, 1], [5, 7, 1], [2, 8, 3], [2, 9, 2], [9, 10, 1]]	2	6
7	6	[[1, 2, 3], [1, 4, 3], [4, 5, 1], [5, 6, 1], [3, 6, 2], [3, 7, 2]]	3	7

파이프 기준으로 그래프 만들어두고, 들어갈 파이프 조합을 구성한 뒤, 이 파이프 구성대로 들어가면서 bfs하고, bfs 하면서 추가되는 노드들의 개수를 더해놨다가 이 값의 최댓값을 저장해 반환하면 되는 문제.
'''

from itertools import product
from collections import deque

def bfs(graph, visited, start, pipe):
    que = deque()
    que.append(start)
    result = 0
    
    while que:
        node = que.popleft()
        for idx, c_node in enumerate(graph[node]):
            if c_node == pipe and visited[idx] == False:
                que.append(idx)
                visited[idx] = True
                result += 1
    return result

def solution(n, infection, edges, k):
    graph = [[None]*(n+1) for _ in range(n+1)]

    answer = 1
    
    for x, y, pipe in edges:
        graph[x][y] = pipe
        graph[y][x] = pipe
    
    for seq in product([1,2,3], repeat=k):
        visited = [False] * (n + 1)
        visited[infection] = True
        tmp_answer = 1
        
        for pipe in seq:
            for i in range(1,n+1):
                # 파이프 열고 나서 이후에 확장된 곳 기준으로 다 확인
                if visited[i] == True:
                    tmp_answer += bfs(graph, visited, i, pipe)
        answer = max(answer, tmp_answer)
        
    return answer
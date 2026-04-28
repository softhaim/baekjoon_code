# 던전 방문 순서에 따라 최대로 탐험할 수 있는 던전 수가 달라진다.
# 따라서 DFS/백트래킹을 사용해서 "현재 피로도에서 갈 수 있는 던전"을 하나씩 선택해보며
# 가능한 모든 방문 경로를 탐색한다.

answer = 0

def dfs(now_k, cnt, dungeons, visited):
    global answer

    # 현재까지 탐험한 던전 수(cnt)가 기존 최댓값보다 크면 갱신한다.
    # DFS가 진행되는 중간 상태도 하나의 가능한 탐험 결과이므로 매번 갱신한다.
    if cnt > answer:
        answer = cnt

    # 모든 던전을 하나씩 확인하면서,
    # 아직 방문하지 않았고 현재 피로도로 입장 가능한 던전이면 탐험한다.
    for i in range(len(dungeons)):
        required, consume = dungeons[i]

        # visited[i] == False: 아직 i번 던전을 방문하지 않음
        # required <= now_k: 현재 피로도가 최소 필요 피로도 이상이므로 입장 가능
        if not visited[i] and required <= now_k:
            # i번 던전을 방문 처리한다.
            visited[i] = True

            # i번 던전을 탐험하면 피로도가 consume만큼 감소하고,
            # 탐험한 던전 수는 1 증가한다.
            # 이후 남은 피로도와 방문 상태를 기준으로 다음 던전을 계속 탐색한다.
            dfs(now_k - consume, cnt + 1, dungeons, visited)

            # 백트래킹:
            # i번 던전을 선택한 경우의 탐색이 끝났으므로 방문 표시를 되돌린다.
            # 그래야 다른 순서에서 i번 던전을 다시 선택해볼 수 있다.
            visited[i] = False

def solution(k, dungeons):
    global answer

    # visited[i]는 i번 던전을 이미 탐험했는지 여부를 저장한다.
    visited = [False] * len(dungeons)

    # 초기 피로도 k, 탐험한 던전 수 0에서 DFS 시작
    dfs(k, 0, dungeons, visited)

    return answer

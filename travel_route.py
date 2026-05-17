'''
문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
입출력 예
tickets	return
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

DFS를 통하여 경로 시작 위치부터 들어가서 모든 항공권 다 연결되는 경로 발견시 return 하고 그 값 기록했다가 그 값 return
'''

answer = []

def dfs(tickets, visited, now, path):
    global answer
    if len(path) == len(tickets)+1:
        answer = path
        return True
    for i in range(len(tickets)):
        a, b = tickets[i]
        if a == now and visited[i] == False:
            visited[i] = True
            if dfs(tickets, visited, b, path+[b]) :
                return True
            visited[i] = False
            
    return False
        
def solution(tickets):
    tickets.sort()
    visited = [False]*(len(tickets))
    dfs(tickets, visited, "ICN", ["ICN"])
    return answer
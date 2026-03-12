'''
백트랙킹 문제.
난 우선 1을 기준으로 팀을 만든다 생각하고 start 를 1 기준해서 넣어서 경우의 수대로 넣어서 팀을 꾸려서 그 팀 숫자가 N의 절반이면 양 팀이 딱 꾸려졌기에 여기서 체크
1과 같은 start 팀인지, 아닌지를 우선 찾고 이 값을 바탕으로 해서 해당하는 팀원들간의 시너지 값들을 합함.
이 합한 두 팀 차이의 min을 저장해두고 출력.
'''

import sys

input = sys.stdin.readline

def backtracking(idx, start):
    global min_diff

    if idx == N//2:
        sum_start_team = 0
        sum_link_team = 0
        start_team = [0]
        link_team = [0]
        for val_idx, val in enumerate(is_start_team[1:], 1): # 1 기준으로 넣었으니까
            if val == False: # 다른팀이면
                link_team.append(val_idx)
            else:
                start_team.append(val_idx)

        for i in range(1,len(start_team)):
            for j in range(i+1,len(start_team)):
                sum_start_team += (arr[start_team[i]][start_team[j]] + arr[start_team[j]][start_team[i]])
        
        for i in range(1, len(link_team)):
            for j in range(i+1, len(link_team)):
                sum_link_team += arr[link_team[i]][link_team[j]] + arr[link_team[j]][link_team[i]]

        min_diff = min(abs(sum_start_team - sum_link_team), min_diff)
        return

    # 짝수명의 절반씩 나눠짐으로인해서 절반 만큼 명수까지 추가 하면 됨.
    # 1 번을 기준으로 짝을 짓는다 생각.
    for j in range(start,N+1):
        if is_start_team[j] != True:
            is_start_team[j] = True       
            backtracking(idx+1,j+1) # j번째 현재 넣고 난 뒤 그 이후의 팀원을 탐색하며 넣도록.
            is_start_team[j] = False
                

if __name__ == "__main__":
    N = int(input())

    arr = [[] for _ in range(N+1)]

    for i in range(1, N+1):
        arr[i] = [0]+(list(map(int,input().split())))
    
    is_start_team = [False]*(N+1)
    is_start_team[1] = True # 1번 기준으로 팀 만들게 1번 넣었다 생각
    
    min_diff = float('inf')
    backtracking(idx=1, start=2)
    print(min_diff)
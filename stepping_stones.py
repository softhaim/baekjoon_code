'''
문제 설명
출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.
예를 들어, 도착지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.

제거한 바위의 위치	각 바위 사이의 거리	거리의 최솟값
[21, 17]	[2, 9, 3, 11]	2
[2, 21]	[11, 3, 3, 8]	3
[2, 11]	[14, 3, 4, 4]	3
[11, 21]	[2, 12, 3, 8]	2
[2, 14]	[11, 6, 4, 4]	4
위에서 구한 거리의 최솟값 중에 가장 큰 값은 4입니다.

출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수로 주어질 때, 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return 하도록 solution 함수를 작성해주세요.

제한사항
도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.
바위는 1개 이상 50,000개 이하가 있습니다.
n 은 1 이상 바위의 개수 이하입니다.
입출력 예
distance	rocks	n	return
25	[2, 14, 11, 21, 17]	2	4


정렬하면 
25 기준으로
0 2 11 14 17 21 25
목표 최솟값을 달성할 수 있는지를 탐색
mid = 1+25 // 2 = 13

바위를 앞에서부터 보면서 현재 바위와 이전 유지한 위치 사이 거리가 mid보다 작으면 그 바위는 제거
이후 n 보다 크다면 이 mid 보다 작은게 너무 많다는 것이니 그 mid-1 으로 right 지정하고 탐색해서 되는지 확인, 만약 최종 n개 이하이면 해당 mid 보다 커서 다 못지웠거나, 최소인경우라 딱 맞는 경우이니 left = mid+1.

'''

def solution(distance, rocks, n):

    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    
    left = 1
    right = distance
    
    while left <= right:
        delete_n = 0
        mid = (left+right)//2
        pos = rocks[0] # pos 두는 이유가 지우면 다음꺼 비교시 지운거 전의 바위랑 비교해야해서
        for i in range(1, len(rocks)):
            if rocks[i] - pos < mid:
                delete_n += 1
            else:
                pos = rocks[i]
        if delete_n > n:
            right = mid - 1
        if delete_n <= n:
            left = mid + 1
    return right
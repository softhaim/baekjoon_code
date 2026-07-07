'''
문제 설명
호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님들을 받으려고 합니다. 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용할 수 있습니다.
예약 시각이 문자열 형태로 담긴 2차원 배열 book_time이 매개변수로 주어질 때, 코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.

제한사항
1 ≤ book_time의 길이 ≤ 1,000
book_time[i]는 ["HH:MM", "HH:MM"]의 형태로 이루어진 배열입니다
[대실 시작 시각, 대실 종료 시각] 형태입니다.
시각은 HH:MM 형태로 24시간 표기법을 따르며, "00:00" 부터 "23:59" 까지로 주어집니다.
예약 시각이 자정을 넘어가는 경우는 없습니다.
시작 시각은 항상 종료 시각보다 빠릅니다.
입출력 예
book_time	result
[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]	3
[["09:10", "10:10"], ["10:20", "12:20"]]	1
[["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]	3

우선순위 큐를 사용하여 가장 빨리 비는 방의 청소 완료 시간을 관리하고, 현재 손님의 입실시간과 비교하여 필요한 최소 객실 수를 계산하는 문제였음. 
우선순위 큐로 가장 작은 청소 완료 시간을 갱신하면서 큐에 지금 운행중인 방의 개수만큼 넣고 끝나는 시간보다 늦은 시간 예약 들어오면 이건 새로운 방이 필요 없으니 기존 방 사용하면 되니까 pop 해서 제거하고 지금 운행중인거 넣음.
'''

import heapq

def solution(book_time):

    for idx, (start, end) in enumerate(book_time):
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))
        
        total_sm = sh*60 + sm
        total_em = eh*60 + em + 10
        book_time[idx] = [total_sm, total_em]
        
    book_time.sort(key=lambda x:x[0])
    
    room_heap = []
    # 가장 빨리 비는 방의 청소 완료 시간이 현재 손님의 입실시간 보다 작거나 같다면, 이어서 쓸 수 있으므로 힙에서 제거
    for start, end in book_time:
        if room_heap and room_heap[0] <= start:
            heapq.heappop(room_heap)
            
        heapq.heappush(room_heap, end)
            
    return len(room_heap)
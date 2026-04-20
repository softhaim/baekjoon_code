from collections import deque
def solution(prices):
    input_prices = deque(prices)
    answer = []
    
    while input_prices:
        val = input_prices.popleft()
        cnt = 0
        for price in input_prices:
            cnt += 1 # 우선 1초가 지났다고 가정
            if val > price: # 가격이 떨어졌다면?
                break # 더 이상 세지 않고 멈춤
        answer.append(cnt)
        
    return answer주식가격

from collections import deque
def solution(number, k):
    stack = deque()
    
    for val in list(number):
        while stack and stack[-1] < val and k != 0:
            k -= 1
            stack.pop()
        stack.append(val)

    # 아직 제거해야 할 숫자가 남았다면 뒤에서 제거
    if k > 0:
        for _ in range(k):
            stack.pop()

    answer = "".join(stack)
    return answer

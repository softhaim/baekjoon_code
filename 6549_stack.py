'''
원래는 이렇게 푸는거라고 함.
핵심 아이디어는:

높이가 증가하는 인덱스를 스택에 넣어둔다

현재 높이가 스택 top보다 낮아지는 순간,
그 top 막대를 높이로 하는 최대 직사각형을 계산한다

각 막대는 스택에 한 번 들어가고 한 번 나오므로 O(n)

시간은 176ms 로 308인 분할정복보다 빠름.
'''
import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    n = arr[0]
    h = arr[1:]
    h.append(0)  # 마지막에 스택을 비우기 위한 더미

    stack = []
    answer = 0

    for i in range(n + 1):
        while stack and h[stack[-1]] > h[i]: # 스택 top 보다 낮아지면 스택에 있는 것들 기준으로 해당 값보다 작아질때 까지 탐색
            height = h[stack.pop()] # 스택에 있는 인덱스의 값을 가져옴

            if stack: # 스택에 값이 있다면 현재 i 번째 부터 해서, 스택의 인덱스까지의 길이를 계산. 이 때 어차피 현재 값이 클때만 넣었기에 아까 위에서 height 는 작아진 값을 기반으로 width 와 곱해서 아래 answer 에서 계산됨. 또한 스택에 idx값으로 들어가 있어서 이후 들어가는 값에서 다시 계산할때도 저 위치까지 width계산이 되고, 그때 width 와 height 곱해짐.
                width = i - stack[-1] - 1
            else:
                width = i

            answer = max(answer, height * width)

        stack.append(i)

    print(answer)
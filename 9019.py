'''
n의 네 자릿수를 d1, d2, d3, d4라고 하자
D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
위에서 언급한 것처럼, L 과 R 명령어는 십진 자릿수를 가정하고 연산을 수행한다. 예를 들어서 n = 1234 라면 여기에 L 을 적용하면 2341 이 되고 R 을 적용하면 4123 이 된다.

딱 봐도 bfs로 저 각 연산별로 데큐에 넣고 뺑뺑이 해서 최소 연산으로 하는거 출력하면 됨. 그과정에서 (num, cmd)해서 cmd에 지금까지 했던거 경로 저장해두고 찾으면 그때의 경로 cmd 출력 하면 됨.
회전 부분이 어떻게 하는지 몰라서 이건 컨닝좀 함.
d = (n * 2) % 10000
s = (n - 1) % 10000
l = n//1000 + (n % 1000) * 10 : n을 1000으로 나눈 값은 앞자리(4자리 고정이니까.) 그리고 n을 1000으로 나눈 나머지가 이후 3자리 값일건데 여기서 10 곱해서 천의자리로 만들고 일의자리에 저 앞자리 수 만큼 더해서 회전하는거.
r = n//10 + (n%10) * 1000  : 비슷하게 10으로 나누면 10의 자리까지의 값일거고, 일의자리는 10으로 나눈 나머지 값인데 여기에 1000 곱해서 천의자리로 보내고 아까 10으로 나눈 값을 이후에 더해서 회전.
'''

import sys
from collections import deque 

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append([A, ""]) # 숫자, 커맨드
    visited = [0]*(10001)

    while que:
        num, cmd = que.popleft()

        if num == B:
            return cmd

        d = (num * 2) % 10000
        s = (num - 1) % 10000
        l = num//1000 + (num%1000)*10
        r = num//10 + (num%10)*1000

        if visited[d] == 0:
            que.append([d, cmd+"D"])
            visited[d] = 1
        if visited[s] == 0:
            que.append([s,cmd+"S"])
            visited[s] = 1
        if visited[l] == 0:
            que.append([l, cmd+"L"])
            visited[l] = 1
        if visited[r] == 0:
            que.append([r, cmd+"R"])
            visited[r] = 1

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        A, B = map(int, input().split())
        print(bfs())


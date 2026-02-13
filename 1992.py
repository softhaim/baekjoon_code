'''
주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다. 
만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축하게 되며, 
이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다

위 그림에서 왼쪽의 영상은 오른쪽의 배열과 같이 숫자로 주어지며, 이 영상을 쿼드 트리 구조를 이용하여 압축하면 "(0(0011)(0(0111)01)1)"로 표현된다.
N ×N 크기의 영상이 주어질 때, 이 영상을 압축한 결과를 출력하는 프로그램을 작성하시오.
'''
import sys

input = sys.stdin.readline

N = int(input())

arr = []
print_arr = []
for i in range(N):
    arr.append(list(map(int, input().strip())))

def is_uniform(x,y,size):
    '''
    시작 원소가 x,y 일 때, 해당 분할 한 영역이 한 원소로만 차있는지 검사하는 함수
    '''
    first = arr[x][y]

    for i in range(x,x+size):
        row = arr[i]
        for j in range(y,y+size):
            if row[j] != first:
                return False, None
    return True, first


def divide(x,y,size):
    '''
    분할해서 쿼드트리로 탐색
    '''
    ok, value = is_uniform(x,y,size)

    if ok:
        if value == 1:
            print_arr.append("1")
        else: # 0 이니까
            print_arr.append("0")
    else:
        # 이 경우 size 가 2 아래면 안되니까 이 경우에는 그냥 ok아니면 그냥 출력하도록 해야함.
        if size <= 2:
            print_arr.extend(["(", arr[x][y], arr[x][y+1], arr[x+1][y], arr[x+1][y+1], ")"])
            return
        else: # 2보다 크면 나눠서 찾을 것이기에
            mid = size//2
            print_arr.append("(")
            divide(x,y, mid) # 1번 사분면
            divide(x,y+mid, mid) # 2번 사분면
            divide(x+mid,y, mid) # 3번 사분면
            divide(x+mid,y+mid, mid) # 4번 사분면 
            print_arr.append(")")
    return

divide(0,0,N)

for val in print_arr:
    print(val, end="")
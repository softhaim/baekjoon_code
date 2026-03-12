'''
1. -가 3N개 있는 문자열에서 시작한다.

2. 문자열을 3등분 한 뒤, 가운데 문자열을 공백으로 바꾼다. 이렇게 하면, 선(문자열) 2개가 남는다.

3. 이제 각 선(문자열)을 3등분 하고, 가운데 문자열을 공백으로 바꾼다. 이 과정은 모든 선의 길이가 1일때 까지 계속 한다.

'''
import sys
input = sys.stdin.readline

def div_3_print(start, end):
    if start+1 == end: # 1차이면 해당꺼 출력해야하는 부분이니까 그대로 둚.
        return
    third = (end - start) // 3
    left_div = (start+third)  # 해당 인덱스 전까지 출력해야함 range(0,left_div)
    right_div = (end-third) # 해당 인덱스 부터 끝까지 출력해야함. range(right_div,num)
    
    div_3_print(start,left_div)
    for i in range(left_div,right_div):
        arr[i] = " "
    div_3_print(right_div, end)

if __name__ == "__main__":
    while True:
        try:
            N = int(input())
            if N == 0:
                print("-")
            else:
                num_text = 3**N
                arr = ["-"]*num_text
                div_3_print(0,num_text)
                print("".join(arr)) # 출력은 이렇게 해야하나봄. 아니면 형식 오류.
        except:
            break
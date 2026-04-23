'''
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
'''

'''
문자열들을 길이 맞춰서 비교 비슷하게 만들기 위해 반복합니다.

"3"   -> "333"
"30"  -> "303030"
"34"  -> "343434"
"5"   -> "555"
"9"   -> "999"

이걸 내림차순 정렬하면

"9", "5", "34", "3", "30"

순서가 나옵니다.

이런식으로 풀 수 있음.

아래는 다른 방법으로 functools로 2개를 합친것을 바탕으로 뭐가 더 큰지를 가지고 비교해서 정렬하도록 하는것인데 정석은 이거.
sorted()는 기본적으로 key=만 받습니다.
그래서 comparator를 바로 못 넣고, 그걸 key처럼 보이게 바꿔주는 게 cmp_to_key. 2개 비교하는 함수를 key로 바꿔주는 것임.

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
'''
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True) # 1000까지니까 세자리 수 까지만 비교
    return str(int(''.join(numbers)))

if __name__ == "__main__":
    print(f'{solution([6, 10, 2])}, gold ANS: 6210')
    print(f'{solution([3, 30, 34, 5, 9])}, gold ANS: 9534330')
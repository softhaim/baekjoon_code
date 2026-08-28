'''
문제 설명
img1.png

네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"
이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

숫자	영단어
0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine
제한사항
1 ≤ s의 길이 ≤ 50
s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

입출력 예
s	result
"one4seveneight"	1478
"23four5six7"	234567
"2three45sixseven"	234567
"123"	123
'''

# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)


def solution(s):
    answer = ""
    # 영단어 앞 2글자를 키로 하고, (숫자값, 추가로 더 건너뛸 길이)를 저장
    num_and_pluslen = {
        'ze':(0,2), 'on':(1,1), 'tw':(2,1), 'th':(3,3), 'fo':(4,2), 
        'fi':(5,2), 'si':(6,1), 'se':(7,3), 'ei':(8,3), 'ni':(9,2) 
    }
    n = len(s)
    idx = 0
    
    while idx < n:
        # 1.문자가 숫자인지
        while idx < n and s[idx].isdigit():
            answer += s[idx]
            idx += 1
            
        # 2. 숫자를 다 파싱한 후 인덱스가 끝에 도달했다면 루프 탈출
        if idx >= n:
            break
            
        # 3. 영단어 처리
        key = s[idx:idx+2]
        num = num_and_pluslen[key] 
        answer += str(num[0])
        idx += 2 + num[1]
        
    return int(answer)

if __name__ == "__main__":
    s = "one4seveneight"
    ans = solution(s)
    print(f"Solution for {s}: {ans}, is_correct: {ans == 1478}") # 1478
    s = "23four5six7"
    ans = solution(s)
    print(f"Solution for {s}: {ans}, is_correct: {ans == 234567}") # 234567
    s = "2three45sixseven"
    ans = solution(s)
    print(f"Solution for {s}: {ans}, is_correct: {ans == 234567}") # 234567
    s = "123"
    ans = solution(s)
    print(f"Solution for {s}: {ans}, is_correct: {ans == 123}") # 123
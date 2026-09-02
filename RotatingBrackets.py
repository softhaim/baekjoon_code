'''
문제 설명
다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.

(), [], {} 는 모두 올바른 괄호 문자열입니다.
만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
s의 길이는 1 이상 1,000 이하입니다.

입출력 예
s	result
"[](){}"	3
"}]()[{"	2
"[)(]"	0
"}}}"	0
'''
from collections import deque

def solution(s):
    # 홀수 길이인 경우 올바른 괄호 문자열이 될 수 없음 (조기 리턴)
    if len(s) % 2 != 0:
        return 0
    
    answer = 0
    
    for i in range(len(s)):
        que = deque()
        is_vaild = True
        
        for c in s[i:] + s[:i]:
            if c in {')', '}', ']'}:
                if (que
                      and (que[-1] == '[' and c == ']' 
                      or que[-1] == '{' and c == '}' 
                      or que[-1] == '(' and c == ')')):
                    que.pop()
                else:
                    is_vaild = False
                    break
            else: # 여는 괄호
                que.append(c)
        
        if is_vaild and not que:
            answer += 1
        
    return answer

if __name__ == "__main__":
    s = "[](){}"
    ans = solution(s)
    print(f"solution(s): {ans} is_correct: {ans == 3}")  # Output: 3
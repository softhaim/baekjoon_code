'''
문제 설명
머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ babbling의 길이 ≤ 100
1 ≤ babbling[i]의 길이 ≤ 30
문자열은 알파벳 소문자로만 이루어져 있습니다.

입출력 예
babbling	result
["aya", "yee", "u", "maa"]	1
["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	2

set으로 permutation을 구해서 가능한 발음들을 만들어서 비교하는 방법을 사용하려 했으나, 몇번이나 반복할 수 있기에, 
연속 발음을 체크하고 허용된 발음을 공백으로 대체한 후 남은 글자가 없으면 발음 가능하다고 판단하는 방법이 더 효율적임
'''

def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        # 1. 같은 발음이 연속으로 2번 나오는지 체크
        for w in words:
            if w * 2 in b:
                break
        else:
            # 2. 연속 발음이 없으면 허용된 발음들을 공백으로 대체
            for w in words:
                b = b.replace(w, " ")
            
            # 3. 공백을 다 지웠을 때 남은 글자가 없으면 발음 가능
            if b.strip() == "":
                answer += 1
                
    return answer
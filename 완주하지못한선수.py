'''문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
입출력 예
participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
입출력 예 설명
예제 #1
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.
'''

from collections import Counter # 리스트나 문자열에서 각 요소의 등장 횟수를 카운팅하는 것 두 데이터 간의 차이나 합집합을 계산하거나, 기존 카운팅 데이터에 새로운 데이터를 추가하는 작업을 간단히 처리할 수 있음.

def solution(participant, completion):
    not_complete = Counter(participant) - Counter(completion) # 각각 사람 대해서 1로 카운팅 한것을 completion 을 빼면 완주 못한 사람만 1 이고 나머진 0 이 될 것임.
    answer = list(not_complete.elements()) # 카운트된 숫자만큼 요소를 반복자(iterator) 형태로 반환하는 기능. 하나 밖에 없으니 하나만 나올거고 이를 리스트로 저장해줌. keys 로 한 뒤 list 로 만들고 해도 동일
    # answer = list(not_complete.keys()) # 동일
    return answer[0]

if __name__ == "__main__":
    participant = list(input().strip().split())
    completion = list(input().strip().split())

    print(solution(participant, completion))
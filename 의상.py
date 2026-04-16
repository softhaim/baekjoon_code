'''
문제 설명
코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.

예를 들어 코니가 가진 옷이 아래와 같고, 오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.

종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트
코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다. 예를 들어 위 예시의 경우 동그란 안경과 검정 선글라스를 동시에 착용할 수는 없습니다.
착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
코니는 하루에 최소 한 개의 의상은 입습니다.
코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
코니가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
입출력 예
clothes	return
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	3

'''

def solution(clothes):
    dict_clothes = {}
    for item, category in clothes:
        dict_clothes[category] = dict_clothes.get(category, 0) + 1 # 키 없으면 0 반환하고 아니면 해당값 반환. 그리고 + 1 해줌 -> 카테고리별 카운트 함.
        
    answer = 1
    for count in dict_clothes.values(): # 카운트 해놓은거 바탕으로 경우의 수 셈.
        answer *= (count+1) # 카테고리 옷 개수 만큼의 해당 옷 선택하여 생기는 경우의 수 + 카테고리에서 아무것도 안입은 경우의 수까지가 경우의 수. 즉 headgear에 2개 있으면 각각 입는 경우, 아예 headgear 안입는 경우로 3개의 경우의 수로 계산한다는 거.
    answer -= 1 # 전부 다 안입는 경우의 수 고른 경우는 제외. 조건 상 하나라도 입어야 하기에.

    return answer

if __name__ == "__main__":
    clothes = []
    while True:
        try:
            input_text = list(input().strip().split())
            if input_text == None or len(input_text) < 2:
                if len(clothes) > 1:
                    print(solution(clothes))
                break
            clothes.append(input_text)
        except:
            break
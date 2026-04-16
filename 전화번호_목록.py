'''문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.

입출력 예제
phone_book	return
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false

'''
def solution(phone_book):
    hash_map = set(phone_book) # set으로 바로 키값으로 찾게 함.
    
    for nums in phone_book: # 리스트의 값에서 하나씩 보면서 set에 있는 값인지 확인. 있다면, 그것이 자기 자신이 아닌 경우, 접두사인것이기에 False 반환.
        arr = ""
        for num in nums:
            arr += num
            if arr in hash_map and nums != arr: # 현재랑 같은것은 아님
                return False
    return True

if __name__ == "__main__":
    phone_book = list(input().split())
    print(solution(phone_book))

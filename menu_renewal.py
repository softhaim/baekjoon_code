'''

'''
# 내가 처음 푼 풀이
from collections import Counter, defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    
    set_counts = Counter()
    len_counts = defaultdict(set)

    for text in orders:
        # 각 단어 내에서 등장한 알파벳으로 2글자 조합 생성
        for i in range(2, len(text)+1):
            for comb in combinations(sorted(text), i):
                txt_comb = "".join(comb)
                set_counts[txt_comb] += 1
                len_counts[len(txt_comb)].add(txt_comb)
                
    for val in course:
        max_val = 0
        max_str = []
        for value in len_counts[val]:
            val_cnt = set_counts[value]
            if val_cnt < 2:
                continue
            if val_cnt> max_val:
                max_val = val_cnt
                max_str = [value]
            elif val_cnt == max_val:
                max_str.append(value)
        for s in max_str:
            answer.append(s)
    
    # 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬
    answer.sort()
    return answer


# 더 효율적으로 질문에 포함된 길이만 조합 생성해서 찾는 풀이
from collections import Counter
from itertools import combinations

def solution_improve(orders, course):
    answer = []
    
    # 각 코스 요리 메뉴 수(c)별로 탐색
    for c in course:
        comb_list = []
        for order in orders:
            # order를 정렬한 후, 원하는 길이 c의 조합만 생성
            comb_list.extend(combinations(sorted(order), c))
            
        # 등장 횟수 카운트
        counter = Counter(comb_list)
        
        # 해당 길이에 조합이 존재하고, 최다 주문 횟수가 2 이상인 경우만 처리
        if counter and max(counter.values()) >= 2:
            max_val = max(counter.values())
            # 최다 주문 횟수(max_val)와 동일한 조합을 모두 선택
            for k, v in counter.items():
                if v == max_val:
                    answer.append("".join(k))
                    
    # 사전 순 오름차순 정렬
    return sorted(answer)

if __name__ == "__main__":
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2, 3, 4]
    ans = solution_improve(orders, course)
    print(f"solution_improve(orders, course): {ans} is_correct: {ans == ['AC', 'ACDE', 'BCFG', 'CDE']}")  # Output: ['AC', 'ACDE', 'BCFG', 'CDE']

    orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    course = [2, 3, 5]
    ans = solution_improve(orders, course)
    print(f"solution_improve(orders, course): {ans} is_correct: {ans == ['ACD', 'AD', 'ADE', 'CD', 'XYZ']}")  # Output: ['ACD', 'AD', 'ADE', 'CD', 'XYZ']

    orders = ["XYZ", "XWY", "WXA"]
    course = [2, 3, 4]
    ans = solution_improve(orders, course)
    print(f"solution_improve(orders, course): {ans} is_correct: {ans == ['WX', 'XY']}")  # Output: ['WX', 'XY']
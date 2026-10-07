'''
문제 설명
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.

U: 위쪽으로 한 칸 가기

D: 아래쪽으로 한 칸 가기

R: 오른쪽으로 한 칸 가기

L: 왼쪽으로 한 칸 가기

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.

방문길이1_qpp9l3.png

예를 들어, "ULURRDLLU"로 명령했다면

방문길이2_lezmdo.png

1번 명령어부터 7번 명령어까지 다음과 같이 움직입니다.
방문길이3_sootjd.png

8번 명령어부터 9번 명령어까지 다음과 같이 움직입니다.
방문길이4_hlpiej.png

이때, 우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다. 예를 들어 위의 예시에서 게임 캐릭터가 움직인 길이는 9이지만, 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다. (8, 9번 명령어에서 움직인 길은 2, 3번 명령어에서 이미 거쳐 간 길입니다)

단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.

예를 들어, "LULLLLLLU"로 명령했다면

방문길이5_nitjwj.png

1번 명령어부터 6번 명령어대로 움직인 후, 7, 8번 명령어는 무시합니다. 다시 9번 명령어대로 움직입니다.
방문길이6_nzhumd.png

이때 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다.

명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.

제한사항
dirs는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
dirs의 길이는 500 이하의 자연수입니다.

입출력 예
dirs	answer
"ULURRDLLU"	7
"LULLLLLLU"	7
'''

def solution(dirs):
    dirs_dic = {"U":(1,0), "D":(-1,0), "R":(0,1), "L":(0,-1)}
    i, j = 0,0
    visited_set = set()
    answer = 0
    
    for val in dirs:
        di, dj = i + dirs_dic[val][0], j + dirs_dic[val][1]
        
        # 범위 밖이거나, set에 기록된 경로인 경우 셀 필요 없음 반대인 경우만 세고 위치값 및 방문 여부 저장
        if -5<=di<=5 and -5<=dj<=5:
            if not (i, j, di, dj) in visited_set: # 다른 사람 풀이 보니 어차피 set이 중복 저장안되게 해서 len(set)으로도 방문한 새로운 길 개수 셀 수 있지만 난 방문 여부로 체크함
                visited_set.add((i, j, di, dj))
                visited_set.add((di, dj, i, j)) # 양방향 다 저장해서 반대 방향이여도 새로운 길로 인식하지 않도록 함.
                answer += 1
            i ,j = di, dj
        
    return answer

if __name__ == "__main__":
    test_cases = [
        ("ULURRDLLU", 7),
        ("LULLLLLLU", 7),
    ]
    
    for dirs, expected in test_cases:
        result = solution(dirs)
        print(f"Input: {dirs}, Output: {result}, Expected: {expected}, is_correct: {result == expected}")
# 입력: [2, 1, 3, 4, 1]  
# 출력: [2, 3, 4, 5, 6, 7]
# 입력수에 중복을 제거하면서 오름차순으로 출력값 정렬하기

def solution(numbers):
    result = set() #set라는 빈 리스트 만들기
    for i in range(len(numbers)): #입력된 숫자 리스트 숫자 개수만큼 i 순회
        for j in range(i+1, len(numbers)): 
            sum_val = numbers[i] + numbers[j]
            result.add(sum_val)
    return sorted(result) #result 결과물 오름차순 정렬


#수포자 3명이 문제를 찍는 패턴을 리스트로 만들어두었음
#각 수포자 3명이 맞춘 개수 출력
def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]  # 각 사람 점수 저장
    
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            score[0] += 1
        if answers[i] == p2[i % len(p2)]:
            score[1] += 1
        if answers[i] == p3[i % len(p3)]:
            score[2] += 1
    
    max_score = max(score)
    result = []
    for i in range(3):
        if score[i] == max_score:
            result.append(i + 1)
    return result

print(solution([1,3,2,4,2,4,4,5,5]))

# 대소문자 구분 없이 문자열 s가 주어졌을 때,
# 그 안에 'p'의 개수와 'y'의 개수가 같으면 True,
# 다르면 False를 반환하는 solution(s) 함수를 완성하세요.

# 입력: "pPoooyY" → 출력: True
# 입력: "Pyy"     → 출력: False

def solution(s):
    s = s.lower()     # 모두 소문자로 변환
    p_count = s.count("p")
    y_count = s.count("y")
    if p_count == y_count:
        return True
    return False

print(solution("pPpppoooyyyyy"))

# 문자열 s가 주어졌을 때,
# 이 문자열이 숫자로만 이루어져 있고,
# 길이가 4 또는 6이면 True, 아니면 False를 반환하세요.

# 입력: "1234"       → 출력: True
# 입력: "a234"       → 출력: False
# 입력: "123456"     → 출력: True
# 입력: "12b34"      → 출력: False
# 입력: "12345"      → 출력: False (길이 5니까!)

def solution(s):
    if (len(s) == 4 or len(s) == 6 ) and s.isdigit():
        return True
    else:
        return False
print(solution("1234asdsd"))


# 캐릭터는 2차원 평면에서 **[0, 0]**에 위치해 있습니다.
# keyinput이라는 문자열 배열이 주어지면,
# 캐릭터는 "up", "down", "left", "right"에 따라 한 칸씩 이동합니다.
# 단, board = [width, height]로 주어진 맵의 범위를 벗어날 수 없습니다.
# 최종 위치 [x, y]를 구하세요.

# 입력:
# keyinput = ["right", "right", "up", "up", "left", "down"]
# board = [5, 5]

# 출력:
# [1, 1]

def solution(keyinput, board):
    x, y = 0, 0
    for key in keyinput:
        if key == "up":
            if y < +(board[1]//2):
                y += 1
        elif key == "down":
            if y > -(board[1]//2):
                y -= 1
        elif key == "right":
            if x < +(board[0]//2):
                x += 1
        elif key == "left":
            if x > -(board[0]//2):
                x -= 1
    return [x, y]
print(solution(["right", "right", "right","down", "up", "up", "left", "down"], [10, 10]))


# 네오가 프로그래밍을 공부하던 중,
# 숫자를 영어로 적은 일부 문장을 숫자로 바꾸는 문제를 만들었습니다.
# 예를 들어 "one4seveneight"은 → 1478로 바뀌어야 해요.

# 입력: "one4seveneight"
# 출력: 1478

# 입력: "23four5six7"
# 출력: 234567

# 입력: "2three45sixseven"
# 출력: 234567

# 입력: "123"
# 출력: 123

def solution(s):
    # 입력 문자열 s에 포함된 영단어 형태의 숫자를 실제 숫자로 변환하고,
    # 최종적으로 변환된 숫자를 거꾸로 뒤집어 반환하는 함수입니다.
    numbers_word = {
        # 숫자를 나타내는 영단어를 key로, 해당하는 숫자 문자열을 value로 하는 딕셔너리입니다.
        "zero" : "0",
        "one"  : "1",
        "two"  : "2",
        "three" :"3",
        "four" :"4",
        "five" :"5",
        "six" :"6",
        "seven" :"7",
        "eight" :"8",
        "nine" :"9"
    }

    # numbers_word 딕셔너리의 각 아이템(영단어와 해당 숫자 문자열)에 대해 반복합니다.
    for word, digit in numbers_word.items():
        # 입력 문자열 s에서 현재 영단어(word)를 찾아 해당 숫자 문자열(digit)로 모두 치환합니다.
        # 예: s가 "one4seven"이고 word가 "one", digit이 "1"이면 s는 "14seven"이 됩니다.
        s = s.replace(word, digit)
    
    # 모든 영단어가 숫자로 치환된 문자열 s를 정수형(int)으로 변환합니다.
    # 예: s가 "123456"이면 num은 정수 123456이 됩니다.
    num = int(s)
    
    # 정수 num을 다시 문자열로 변환한 후, 문자열 슬라이싱([::-1])을 사용하여 순서를 거꾸로 뒤집습니다.
    # 뒤집힌 문자열을 다시 정수형으로 변환하여 reversed_num에 저장합니다.
    # 예: num이 123456이면, str(num)은 "123456", str(num)[::-1]은 "654321", int("654321")은 654321이 됩니다.
    reversed_num = int(str(num)[::-1])
    
    # 최종적으로 뒤집힌 숫자를 반환합니다.
    return reversed_num

print(solution("one4seveneight"))



# 문자열 s가 주어집니다.
# 문자열 안에는 영어 숫자 단어("zero""nine")와 숫자(09)가 섞여 있습니다.
# 이 문자열을 숫자로 바꾸고 뒤집은 정수를 반환하세요.

def solution(s):
    # 입력 문자열 s에 포함된 영단어 형태의 숫자를 실제 숫자로 변환하고,
    # 최종적으로 변환된 숫자를 거꾸로 뒤집어 반환하는 함수입니다.
    numbers_word = {
        # 숫자를 나타내는 영단어를 key로, 해당하는 숫자 문자열을 value로 하는 딕셔너리입니다.
        "zero" : "0",
        "one"  : "1",
        "two"  : "2",
        "three" :"3",
        "four" :"4",
        "five" :"5",
        "six" :"6",
        "seven" :"7",
        "eight" :"8",
        "nine" :"9"
    }

    # numbers_word 딕셔너리의 각 아이템(영단어와 해당 숫자 문자열)에 대해 반복합니다.
    for word, digit in numbers_word.items():
        # 입력 문자열 s에서 현재 영단어(word)를 찾아 해당 숫자 문자열(digit)로 모두 치환합니다.
        s = s.replace(word, digit)
    
    # 모든 영단어가 숫자로 치환된 문자열 s를 정수형(int)으로 변환합니다.
    # 예: s가 "123456"이면 num은 정수 123456이 됩니다.
    num = int(s)
    
    # 정수 num을 다시 문자열로 변환한 후, 문자열 슬라이싱([::-1])을 사용하여 순서를 거꾸로 뒤집습니다.
    # 뒤집힌 문자열을 다시 정수형으로 변환하여 reversed_num에 저장합니다.
    # 예: num이 123456이면, str(num)은 "123456", str(num)[::-1]은 "654321", int("654321")은 654321이 됩니다.
    reversed_num = int(str(num)[::-1])
    
    # 최종적으로 뒤집힌 숫자를 반환합니다.
    return reversed_num

print(solution("one234fivesix"))

# [문제 설명: 비밀 지도]
# 두 개의 정수 배열 arr1, arr2가 주어집니다.
# 각 배열의 원소는 십진수 정수이며, 이 정수를 이진수로 변환했을 때 각 자리는 지도 한 칸을 의미합니다.
# (예: n=5일 때, 9는 이진수로 01001)
# 두 지도를 겹친다고 생각하고, 두 지도 중 어느 하나라도 벽('#', 이진수 '1')인 부분은 전체 지도에서도 벽('#')이 됩니다.
# 두 지도 모두 공백(' ', 이진수 '0')인 부분은 전체 지도에서도 공백(' ')이 됩니다.
# 즉, 각 위치에 대해 OR 연산을 수행하는 것과 유사합니다 (1 | 1 = 1, 1 | 0 = 1, 0 | 1 = 1, 0 | 0 = 0).
# 이렇게 생성된 비밀 지도를 문자열 배열 형태로 반환하는 함수를 작성합니다.

def solution(n, arr1, arr2):
    # n: 지도의 한 변의 크기 (정사각형 지도)
    # arr1: 첫 번째 지도 암호 정보 (정수 배열)
    # arr2: 두 번째 지도 암호 정보 (정수 배열)
    
    result = [] # 최종적으로 생성될 비밀 지도(문자열 배열)를 저장할 리스트
    
    # 지도의 각 행(row)에 대해 반복합니다 (0부터 n-1까지).
    for i in range(n):
        # arr1[i]와 arr2[i]는 각각 첫 번째 지도와 두 번째 지도의 i번째 행에 대한 암호입니다.
        
        # 1. arr1[i]를 이진 문자열로 변환합니다.
        #    bin() 함수는 "0b" 접두사를 붙여 반환하므로 [2:] 슬라이싱으로 제거합니다.
        #    zfill(n)은 문자열의 길이가 n이 되도록 왼쪽에 '0'을 채워줍니다.
        #    예: n=5, arr1[i]=9  -> bin(9)='0b1001' -> '1001' -> '01001'.zfill(5) -> '01001'
        bin1 = bin(arr1[i])[2:].zfill(n)
        
        # 2. arr2[i]를 동일한 방식으로 이진 문자열로 변환합니다.
        #    예: n=5, arr2[i]=30 -> bin(30)='0b11110' -> '11110' -> '11110'.zfill(5) -> '11110'
        bin2 = bin(arr2[i])[2:].zfill(n)
        
        merged_row_str = "" # 현재 행의 지도 문자열을 만들기 위한 빈 문자열 초기화
        
        # 3. 두 이진 문자열(bin1, bin2)의 각 비트(문자)를 비교하여 지도 행을 만듭니다.
        #    zip(bin1, bin2)는 두 문자열의 각 문자를 짝지어 순회합니다.
        #    예: bin1='01001', bin2='11110'
        #        첫 번째 순회: bit1='0', bit2='1'
        #        두 번째 순회: bit1='1', bit2='1'
        #        ...
        for bit1, bit2 in zip(bin1, bin2):
            # 두 비트 중 하나라도 '1'이면 (벽이면) 결과 지도에서도 '#'(벽)으로 표시합니다.
            if bit1 == '1' or bit2 == '1':
                merged_row_str += "#"
            # 두 비트 모두 '0'이면 (공백이면) 결과 지도에서도 ' '(공백)으로 표시합니다.
            else:
                merged_row_str += " "
        
        # 완성된 현재 행의 지도 문자열을 result 리스트에 추가합니다.
        # 예: merged_row_str = "# # # #" (위 예시의 경우)
        result.append(merged_row_str)
        
    # 모든 행에 대한 처리가 끝나면 비밀 지도(문자열 배열)를 반환합니다.
    return result

# 함수 테스트
# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
# 기대 출력:
# ["#####", "# # #", "### #", "#  ##", "#####"]
print("--- 비밀 지도 --- ")
output_map = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
for row in output_map:
    print(row)



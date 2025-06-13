def get_average(scores): #scores의 평균 구하는 함수 정의
    total = 0 # 점수들의 합계를 저장할 변수
    for score in scores: #scores를 score에 순회
        total += score # 각 점수를 total에 누적해서 더함
    return total / len(scores) # socres의 숫자를 토탈로 나눈 후 반환

print(get_average([80, 90, 100]))


def filter_even(numbers): #짝수 판별 숫자 함수 정의
    result = [] #리스트 빈 주머니 생성
    for n in numbers: #numbers을 n 변수에 순회
        if n % 2 == 0: # numbers에 있는 수중에 순회하면서 2로 나누고 0이면
            result.append(n) #짝수인 n을 결과 리스트에 추가
    return result #조건에 맞는 결과 리스트 반환

print(filter_even([1, 2, 3, 4, 5, 6]))

def count_vowels(text):
    #모음의 숫자를 세는 함수 정의
    vowels = "aeiou" #모음값 변수 정의
    count = 0 #숫자를 세기 위한 변수 설정
    for char in text.lower(): #소문자로 모두 바꾼 후에 char 변수값에 순회
        if char in vowels: #모음값이 char값에 포함되는게 있는지는지
            count += 1 #숫자 하나씩 늘려가면서 숫자 세ㅣ
    return count #숫자값 반환

print(count_vowels("Hello World")) #e,o,o 3개 결과값 반환

def reverse_string(s): #문자열 거꾸로
    result = "" #문자열을 배치하여 저장할 변수
    for char in s.lower(): #s 소문자로 변환 후 char이라는 변수값에 순회
        result = char + result #순회한 char을 하나씩 결과값에 추가
    return result
print(reverse_string("Python"))


def factorial(n):
    if n == 0: #n이 0이면,
        return 1 #1을 반환한다.
    return n * factorial(n - 1) #n이 0이 되기전까지 계속 곱하고 출력

print(factorial(5)) #5*4*3*2*1 = 102의 결과값 출력


def is_palindrome(word): 
    return word == word[::-1] #word를 drow로 교체

print(is_palindrome("level")) #거꾸로 해도 같으면 True
print(is_palindrome("apple")) #거꾸로 하면 다른 결과로 Fasle
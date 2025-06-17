# 예제1
words = ["hello", "world"]
uppercased = list(map(str.upper, words))
print(uppercased)

words = ["MINI", "BIG"]
lowercased = list(map(lambda w:w.lower(),words))
print(lowercased)

# 예제2
words = ["python", "java", "c++", "go"] #words 변수에 리스트 
capitalized = list(map(lambda w:w.capitalize(), words)) #words 리스트에서 하나씩 꺼내 단어 맨 앞자를 대문자로 바꾸는 람다 함수
print(capitalized) #["Python", "Java", "C++", "Go"]리스트 출력

# 예제3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #numbers 리스트
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #even_numbers라는 변수에 numbers라는 리스트에서 하나씩 꺼내 그 값이 2로 나눴을때 0인 리스트
print(even_numbers) #[2,4,6,8,10] 출력

numbers2 = [1,2,3,4,5,6,7,8,9,10,11,12]
odd_numbers = list(filter(lambda x: x % 2 == 1, numbers2))
print(odd_numbers)

# 예제4
nums = [-5, 0, 3, 7]
positive = list(filter(lambda x: x > 0, nums))
print(positive)

words = ["hi", "hello", "world", "a", "python"]
long_words = list(filter(lambda w: len(w) >= 5, words))
print(long_words)

# 예제6
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]

# paired = list(zip(names, scores)) #튜플을 묶은 리스트로 만든다[('Alice',85),('Bob',92),('Charlie',78)]

# for name, score in paired: #paired에서 묶은 것 이름과 점수로 순회하면서 하나씩 출력
#     print(f"{name} scored {score} points.") #이름, 점수 출력

names = ["Dino", "David", "Miguel"]
scores = [100,80,70]

paired = list(zip(names, scores))

for names, scores in paired:
    print(f'{names}의 점수는 {scores}점입니다')

# 예제7
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits): #fruits의 리스트를 순회하면서 리스트의 인덱스와 각 요소를 추출 
    print(f"{index}: {fruit}")

colors = ["red","yellow", "black", "white", "blue"]

for i, color in enumerate(colors):
    print(f'{i}에는 {color} 있습니다.')

# 예제8
def get_benefit(user_type): #user_type 함수 정의
    benefits = { #혜택과 관련된 dict타입
        "gold": "Free delivery + 10% discount",
        "silver": "Free delivery",
        "bronze": "2% discount"
    }
    return benefits.get(user_type, "No benefits available") #dict타입에 없는 리스트는 "No benefits available" 은 기본값으로 (안전하게 처리)

user_types = ["gold", "bronze", "vip", "silver"] #user_types 리스트 정리

for u in user_types: #user_types에 리스트들 하나씩 꺼내어 u에 순회
    print(f"{u.upper()} → {get_benefit(u)}") #u 하나씩 꺼내서 대문자, 그리고 key값 꺼내서 출력

# 예제9
scores = [95, 67, 80, 45, 88, 73]
# grades = ["A" if s >= 90 else "B" if s >= 80 else "C" if s >= 70 else "D" if s >= 60 else "F" for s in scores]
grades = ["A" if s >=90 else "B" if s >= 80 else "C" if s >= 70 else "D" if s >= 60 else "F" for s in scores]
print(grades)

# 예제10
from collections import Counter #내장 라이브러리 Counter 사용
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"] #fruits 변수에 과일 리스트
fruit_counts = Counter(fruits) #fruit_counts 변수에 카운터 사용해서 해당하는 '과일 단어' 숫자 추출
most_common = fruit_counts.most_common(1) #추출된 과일 리스트 중 숫자가 큰 대로 나열
print(fruit_counts)
print(most_common)


# 함수 예제 1
def grade_student(score): #학생 계산 점수
    if score >= 90: #90점 이상은 A
        return "A"
    elif score >= 80: #80점 이상은 B
        return "B"
    elif score >= 70: #70점 이상은 C    
        return "C"
    elif score >= 60: #60점 이상은 D
        return "D"
    else: #60점 미만은 F
        return "F"

print(grade_student(85))
print(grade_student(59))
print(grade_student(70))
print(grade_student(65))

# 함수 예제 2
def add(x, y): #더하기 함수
    return x + y

def subtract(x, y): #빼기 함수
    return x - y

def operate(op, a, b): #연산 함수
    operations = {
        "add": add,
        "sub": subtract
    }
    if op in operations:
        return operations[op](a, b)
    else:
        return "Invalid operation"

print(operate("add", 5, 3))
print(operate("sub", 10, 4))
print(operate("mul", 2, 2))

# 함수 예제 3
def categorize_age(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teen"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

ages = [8, 15, 25, 70]
categories = [categorize_age(age) for age in ages] #ages 리스트의 각 요소를 age에 하나씩 넣고, categorize_age() 함수에 전달한
#결과들을 리스트로 만들어 categories에 저장한다.
print(categories)

# 함수 예제 4
def get_discounted_price(category, price):
    discounts = {
        "student": 0.2,
        "veteran": 0.3,
        "senior": 0.15
    }
    rate = discounts.get(category, 0) # get_discounted_price의 category에 0을 채워넣어 rate 변수에 넣는다.
    return price * (1 - rate) #1에서 rate 변수를 뺀후 가격과 곱해서 반환

print(get_discounted_price("student", 100))
print(get_discounted_price("vip", 100))
print(get_discounted_price("senior", 200))

# 함수 예제 5
students = [
    {"name": "Alice", "score": 82}, #이름과 스코어 값을 딕셔너리에 넣어준다.
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 78}
]

sorted_students = sorted(students, key=lambda x: x["score"], reverse=True) # 학생을 점수 기준으로 오름차순 하여 변수 sorted_students에 넣어라.
for s in sorted_students: # 변수에 담긴 것을 순회하여 s 변수에 넣어라
    print(s["name"], s["score"]) # s변수의 이름과 성적을 뽑아라

# 함수 예제 6
numbers = [1, 2, 3, 4, 5, 6]

squared = list(map(lambda x:x**2, numbers))
print(squared)

squared = list(map(lambda x: x ** 2, numbers)) #[1,4,9,16,25,36]
even_squared = list(filter(lambda x: x % 2 == 0, squared))

print(even_squared)

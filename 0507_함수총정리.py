"""
1세대 - 기계어와 어셈블리어(기계쪽에 가까움)
2세대 - 고급언어(사람의 말과 유사한), 코볼, 포트란, 범용언어
    코볼 - 데이터 처리 전문(시장 끝), 포트란 - 과학기술계산용(물리학과, 원자력발전소)
    스파게티 코드 - 대충 의식의 흐름대로 프로그램을 함
    goto - 아무데로나 막 점프한다. 현재는 시스템 프로그램 분야 외 거의 안씀
3세대 - C, algol, pacal 등등....
    스파게티 코드에 대한 반성, 구조적 프로그래밍
    구조적 프로그래밍의 특징
    1. top - down 설계 방식 기본부터 시작해서 아래로 내려가는 방식의 설계
    2. 설계라는 개념을 처음 시도를 한다.
    3. 순서도
    4. 모듈화(함수와 프로시저로 프로그램을 작은 단위로 나누어서 프로그램을 한다)
    5. 주석을 열심히....
    6. 소프트웨어 공학
4세대 - 객체지향 프로그램, 3세대의 반성
1. bottom - up 방식 : 3세대 경험을 바탕으로 부품화(부품 모으면 완제품 된다)
2. 객체지향
    1) 추상화 : 내부의 상세한 내용을 구체적으로 몰라도 사용에 아무 제한 사항이 없는
    성격을 말함 (list 타입, tuple타입, dict타입 등)
    사용자는 내부 구조를 몰라도 된다
    추상화가 될수록 사용자가 편하다
    2) 은닉성 : 데이터를 감춘다.
        컴퓨터의 case가 없으면 오염으로부터 취약하다
        데이터를 보호하자
        접근권한을 만들어서 외부로 접근을 막는다.
        최근에는 이 성격이 약화되고 있다.
        대표적으로 파이썬의 경우 전부 사용 가능하다.
    3) 상속성 : 코드의 재활용도를 높인다. 프레임워크
    코드를 처음부터 짜는게 아니라 이미 만들어놓은 클래스들중에서
    유사한거 골라서 상속받아서 만든다.
    4) 다형성 : 같은 이름의 함수가 다른 기능을 할 수 있다.
        오버로딩 : 같은 이름의 함수가 다른 기능을 할 수 있다.(자바)
        오버라이딩 : 상속받은 클래스에서 같은 이름의 함수가 다른 기능을 할 수 있다.(자바))
        매개변수 기본값 : 파이썬

def 함수이름():
    ....
    ....

함수이름 규칙은 변수 규칙과 동일하다.
    1. 영문자로 시작하고 "-" 가능
    2. 대소문자 구분
    3. 예약어 안됨
    묵시적 : 파이썬은 묵시적 타입 선언이 없다.
    4. 소문자로 시작한다.
    5. 카멜 표기법 또는 스네이크 표기법

전역변수
함수안에서 변수를 사용하면 값을 읽는게 아니고 값을 할당하면,
외부에 있는 전역변수를 가려버린다.

def 함수이름(매개변수):
    ...
    ...


"""
global_x = 10
def myfunc1():
    #함수 내부에 변수에 값을 할당하는 순간 별도의 변수가 만들어진다.
    #예외적으로 외부 변수를 사용하고 싶다면 global 키워드를 사용한다.
    global global_x
    global_x = 30 #global_x는 지역변수 
                #함수 내부에서만 존재하는 변수이다.
    y = 20
    print(global_x, y)

global_x = 100
myfunc1()
print(global_x) #30이 출력되기를 원한다.

##함수의 매개변수 기본값  
##dict로 받을때도 호출하는 방식은 유사하다

def myfunc2(name="홍길동", age=20, tel="010-1234-5678"):
    print(name)
    print(age)
    print(tel)

#이러한 예시가 다형성의 특징이다. 이게 오버로딩 특징?
myfunc2()
myfunc2("임꺽정", 33)
myfunc2(name="둘리")
myfunc2(age=23)
myfunc2(tel="8-48883")

#함수를 동적으로 결정된다. 함수를 미리 만들어놓고 호출하면 정적으로 결정할 수 있는데
#싫행할때 함수가 결정되는 것을 동적 결정
#컴파일러 언어들의 경우에는 컴파일 시간과 실행시간으로 나뉜다.
#컴파일 시간에 결정되면 정적할당, 실행시간에 결정되면 동적할당
#자바는 컴파일러인데도 동적할당이 가능하다.
#파이썬은 모든 것이 실행시간에 결정된다. 즉 동적할당이다.
#
# 제너레이터(개념만) - 우리가 막 만들어 써야 하는 것은 아니고 용어 자체가 중요
# 값을 하나씩 생성해서 순회할 수 있는 함수나 객체(range, filter, map 등이 해당)
print(range(1,6)) #range라는 함수는 for문 안에서 호출하면 데이터 한개씩 만들어서 던져준다.
for i in range(1,6):
    print(i)

#함수안에서 값을 반환하려면 return과 yield가 있다.
#return은 함수를 종료하고 값을 반환한다.
#yield는 값을 반환하고 함수를 종료하지 않는다.
#yield는 제너레이터 함수에서 사용된다.
#제너레이터 함수는 값을 하나씩 생성해서 순회할 수 있는 함수이다.

def myrange(start=1, end=5):
    i = start
    while i <= end:
        yield i #이 구문을 만나는 순간 값을 하나 반환하고 멈춘다.
        i += 1

for i in myrange():
    print(i)

gen = myrange() #함수 호출해서 결과 저장해놓고 next를 통해서 호출한다.
#이때 제너레이터 객체가 따로 만들어진다. 내부적으로 파이썬이 일반함수를 제너레이터 객체로
#만들어서 객체 참조를 gen한테 전달 myrange(함수 -> 제너레이터로 변환)
#next나 for문으로
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for i in myrange(1,10):
    print(i)

"""
1. 데이터가 너무 커서 한번에 생성할 수 없을때
2. 무한한 작업이 필요할때
3. 파일을 계속 읽어서 처리하고자 할때
"""

"""
문제1
입력화면 : 1. 원의 면적 2. 사각형 면적 3. 사다리꼴 면적 0.종료
1을 누르면
반지름 :5
면적은 5*5*3.14
면적 결과 : 78.5
2를 누르면
가로 : 10
세로 : 20
면적은 10*20
면적 결과 : 200
3을 누르면
윗변 : 10
아랫변 : 20
높이 : 30
면적은 (10+20)*30/2
면적 결과 : 450
0을 누르면 종료
"""
def circle():
    radius = int(input("반지름 : "))
    area = radius * radius * 3.14
    print(f"원의 면적은 {area}")

def rectangle():
    width = int(input("가로 : "))
    height = int(input("세로 : "))
    area = width * height
    print(f"사각형의 면적은 {area}")

def trapezoid():
    top = int(input("윗변 : "))
    bottom = int(input("아랫변 : "))
    height = int(input("높이 : "))
    area = (top + bottom) * height / 2
    print(f"사다리꼴의 면적은 {area}")

while True:
    menu = int(input("1. 원의 면적 2. 사각형 면적 3. 사다리꼴 면적 0.종료"))
    if menu == 0:
        break
    elif menu == 1:
        circle()
    elif menu == 2:
        rectangle()
    elif menu == 3:
        trapezoid()
    else:
        print("잘못된 메뉴 선택입니다.")


##강사님 풀이
def circle():
    r = int(input("반지름 : "))
    s = r * r * 3.14
    print(f'원의 면적은 {s:.2f}')

def rectangle():
    w = int(input("가로 : "))
    h = int(input("세로 : "))
    s = w * h
    print(f'사각형의 면적은 {s}')

def sadari():
    t = int(input("윗변 : "))
    b = int(input("아랫변 : "))
    h = int(input("높이 : "))
    s = (t + b) * h / 2
    print(f'사다리꼴의 면적은 {s:.2f}')

def main2():
    myfunctions = {"1": circle, "2": rectangle, "3": sadari}
    while True:
        print("\n=== 도형 면적 계산기 ===")
        print("1. 원의 면적")
        print("2. 사각형 면적")
        print("3. 사다리꼴 면적")
        print("0. 종료")
        select = input("\n메뉴를 선택하세요: ")
        
        if select == "0":
            print("프로그램을 종료합니다.")
            break
        elif select in myfunctions:
            myfunctions[select]()
        else:
            print("잘못된 메뉴 선택입니다.")

main2()

#문제2 리스트를 받아가서 리스트 안에 중복된 데이터를 제거하고 중복되지 않는 데이터 리스트만 반환하기
def remove_duplicates(lst):
    return list(set(lst))
#중복 제거 테스트
test_list = [1,2,3,1,2,3,4,5,1,2,3,4,5]
print("원본 리스트:", test_list)
print("중복 제거된 리스트:", remove_duplicates(test_list))

test_list2 = ["사과","배","사과","귤","배","포도"]
print("원본 리스트:", test_list2) 
print("중복 제거된 리스트:", remove_duplicates(test_list2))

#문제3 myint함수 문자열을 받아서 정수로 바꿔서 반환하기. "123"을 넣었을 경우에는 123을 반환하고
#123a 잘못된 데이터를 입력하면 -1을 반환하기
def myint(s):
    if not s:
        return -1
    sign = 1
    if s[0] == "+":
        s2 = s[1:]
    elif s[0] == "-":
        s2 = s[1:]
        sign = -1
    else:
        s2 = s
    if s2.isdigit():
        return sign * int(s2)
    else:
        return -1
    
print(myint("123"))
print(myint("+7"))
print(myint(" 55"))

##강사님 풀이
def duplicate_remove(lst):
    temp = []
    for i in lst:
        if i not in temp:
            temp.append(i)
    return temp

a = [1,2,3,1,2,3,4,5,1,2,3,4,5]
b = duplicate_remove(a)
print(b)

def myint(s):
    sum = 0
    for c in s:
        if ord(c) < ord('0') or ord(c) > ord('9'):
            return -1
        sum = sum * 10 + (ord(c) - ord('0'))
    return sum

print(myint("123"))
print(myint("   123"))

#문제4 문장을 받아가서 문자열 뒤집어서 보내는 함수 reverse
def reverse(s):
    return s[::-1]

print(reverse("Hello"))
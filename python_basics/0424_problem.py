# """"
# 문제1) m을 km와 m로 전환하기
# 2300미터는 2km와 300미터입니다.
# 미터를 입력받아 각각 km과 m로 전환해서 출력하세요
# 힌트) 몫구하는 연산자 // 나머지 구하는 연산자 %

# 2300 - (2*1000)
# 2300 % 1000
# """
# meter = int(input("미터는?"))
# km = meter // 1000
# m = meter % 1000

# #숫자 문자를 섞어서 출력할 때는 +말고 포맷을 활용한다.
# # fstring, python 3.6부터 추가
# #f를 붙이고 {변수명 또는 수식}
# print(f"{meter} 는 {km}km와 {m}meter 입니다 ")

# km_m = 2
# m_km = 300

# print = 2 // 


# # 문제2) 사다리꼴이 면적 구하기
# # 사다리꼴 면적 : (윗변 + 아랫변) * 높이 / 2

# up = int(input("윗변 :"))
# bottom = int(input("아랫변 :"))
# height = int(input("높이 :"))

# area = int((up + bottom) * height / 2)
# print(f"사다리꼴의 면적은 {area} 입니다")

# del print

# # 문제3) 철수가 식료품점에 가서 과일을 샀다. 사과와 배를 샀는데 사과는
# #         한개에 5000원이고 배는 10000원이다. 각각 사과와 배의 개수를 
# #         입력받아 총금액을 구하는 프로그램을 작성하시오

# apple = 5000
# pear = 10000

# count_apple = int(input("사과는 개수는?"))
# count_pear = int(input("배의 개수는?"))

# sum = (apple * count_apple) + (pear * count_pear)

# print(f"사과와 배의 총금액은 {sum}원 입니다")

# """
# 문제4) 거스름돈 계산하기 - 10만워 짜리를 넣고 거스름돈 받기
# 물건값이 총 : 27560원
# 거스름돈 : 72440
# 50000 - 1장
# 10000 - 2장
# 5000 - 0장
# 1000 - 2장
# 500 - 0개
# 100 - 4개
# 10 - 4개
# """

sum = 100000
pay = 27560
change = 72440

# #입력값 : 사용한 돈 // 내가 푼 문제
# use_money = int(ipunt("사용한 돈"))
# change = 
# fifty_thousand = change // 50000 #50000원
# change = change % 50000 # 22440원 나머지
# ten_thousand = change // 10000 # 20000원
# change = change % 10000 # 2440원
# one_thousand = change // 1000 # 2000원
# change = change % 1000 # 440원
# one_hundred = change // 100 # 400원
# change = change % 100 # 40원
# ten = change // 40 # 40원
# change = change % 40 # 0원

# #중간계산은 거스름돈

# #출력이 나와야겠지?
# print(f"50000원권 : {fifty_thousand}장")
# print(f"10000원권 : {ten_thousand}장")
# print(f"1000원권 : {ten_thousand}장")
# print(f"100원권 : {one_hundred}개")
# print(f"10원권 : {ten}개")


# 강사님 풀이법

use_money = int(input("사용한 돈은?"))
change_money = 100000 - use_money
print("거스름돈", change_money)

temp = change_money
m50000 = temp // 50000
temp = temp % 50000 # temporary(임시)
m10000 = temp // 10000
temp = temp % 10000
m5000 = temp // 5000
temp = temp % 5000
m1000 = temp // 1000
temp = temp % 1000
m500 = temp // 500
temp = temp % 500
m100 = temp // 100
temp = temp % 100
m10 = temp // 10

print("50000 =>", m50000, "장")
print("10000 =>", m10000, "장")
print("5000 =>", m5000, "장")
print("1000 =>", m1000, "장")
print("500=>", m500, "개")
print("100->", m100, "개")
print("10->", m10, "개")열

# 문제5)
# 문제5) 문자열 연습하기
# 5-1 변수에 값 "홍길동, 임꺽정, 장길산, 최영, 윤관, 강감찬, 서희, 이순신, 남이"
# 5-2 => list타입으로 전환
# 5-3 => "서희" 가 몇번째에 있는지
# 5-4 => "이순신"과 "장영실" 존재여부 확인
# 5-5 => 추가할사람: "정도전","정약용","최치원",,,
# 5-6 => "서희" => "김종서" 로 바꾸기
# 5-7(어려움) 장길산 => 김길산 첫글자만 바꾸기 (I think replace?)

## 강사님 풀이법 (5-1,2)
names = "홍길동,임꺽정,장길산,최영,윤관,강감찬,서희,이순신,남이"
print(names, type(names))
name_list = names.split(",") # 전달된 값으로 문자열 쪼개서 => 리스트 타입으로 반환
print(name_list, len(name_list)) #list, 배열의길이

#인덱싱 list, string 경우에 각 요소를 숫자를 통해서 접근 가능하다
print(name_list[0])

#슬라이싱 [시작값:종료값:증감치] 각각 생략 가능하다.
print(name_list[3:]) #3번째 이후 출력(:방향->)
print(name_list[:3]) #3번째 이전 출력(:방향<-)
print(name_list[::-1]) #역순으로 출력 가능
print(name_list[2:5]) #2,3,4번째만 출력

## 강사님 풀이법 (5-3)
print("서희의 위치", name_list.index("서희")) #왜 출력이 안되지?
if name_list.count("이순신") > 0 : #if 조건식 1=True, 0=Fasle / 0이 아니면 모두 True
    print("이순신이 존재한다")
else:
    print("이순신이 존재하지 않는다")
if "장영실" in name_list:
    print("'장영실'이 존재한다.")
else:
    print("'장영실'이 존재하지 않는다.")

print(name_list.count("이순신"), "장영실" in name_list)

## 강사님 풀이법 (5-4)
# name_list.append("정도전")
# name_list.append("정약용")
# name_list.append("최치원")

name_list.extend(["정도전", "정약용", "최치원"])
print(name_list)

## 강사님 풀이법 (5-5)
pos = name_list.index("서희") #서희 위치값을 찾아서 반환받는다.
name_list[pos] = "김종서" #그 위치값에 다른 값을 넣는다.
print(name_list)

## 강사님 풀이법 (5-6)
# 문자열의 경우에는 index를 통한 수정이 불가능하다.
pos = name_list.index("장길산")
name_list[pos] = name_list[pos].replace("장","김")
print(name_list)



### 아래는 내가 풀어놓은 것

# #5-1 문제(변수에 값 지정)
# exl_person = ["홍길동", "임꺽정", "장길산", "최영", "윤곽", "강감찬", "서희", "이순신", "남이"]
# #5-3 "서희" 몇번째 -> 6번째
# exl_person.index("서희")
# #5-4 "이순신" "장영실" 존재 여부
# name_to_find1 = "이순신"
# name_to_find2 = "장영실"
# exists1 = name_to_find1 in exl_person
# exists2 = name_to_find2 in exl_person
# print(exists1)
# print(exists2)
# #5-5 "정도전", "정약용", "최치원" 추가
# extra_person = ["정도전", "정약용", "최치원"]
# exl_person.append(extra_person)
# print(exl_person)
# #5-6 => "서희" => "김종서" 로 바꾸기
# idx = exl_person.index("서희")
# exl_person[idx] = "김종서"
# print(exl_person)
# #5-7 장길산을 '김'길산으로 바꾸기
# idx = exl_person.index("장길산")
# original = exl_person[idx]
# print(original)
# given = original[1:]
# print(given)
# new_name = "김" + given
# print(new_name)
# exl_person[idx] = new_name
# print(exl_person)
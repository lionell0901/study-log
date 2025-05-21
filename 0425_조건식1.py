# #정수를 하나 입력 받아서 양수일 경우 본래의 값에 *5를 해서 출력하라
# n = int(input("정수 :"))
# if n>0 :
#     n=n*5
# print(n)

# #양수이면 양수라고 출력하고 음수나 0이면 양수가 아니라고 출력하라
# if n > 0:
#     print("양수")
# else:
#     print("양수 아님")

n = int(input("정수는"))
if n > 0:
    print("양수")
else:
    print("양수 아님")

# #양수이면 양수 0 음수
# if n>0:
#     print("양수")
# elif n==0:
#     print("0")
# else:
#     print("음수")


#문제1. 주급계산: 이름, 근무시간, 시간당급여액, 추가수당 : 근무시간이 20시간을 초과하면 시간당급여액에 50% 가산한다
#  이름  근무시간 시간당급여액 기본금액   수당    총액
 # 홍길동   30     10000  300000  50000  350000
    
# name = input("이름은?")
# work_time = int(input("근무시간은?"))
# per_pay = int(input("시간당급여액은?"))
# sum = work_time*per_pay

# if work_time > 20:
#     per_pay*0.5
# else:
#     per_pay
# print(per_pay)

 #-----강사님 풀이
# 입력: 이름(name), 근무시간(work_time), 시간당급여액(per_pay)
# 출력:  기본금(base_pay), 수당(over_pay), 총액(total_pay)
# 1. 입력 2. 계산 3. 출력
"""
name = input("이름은?")
work_time = int(input("근무시간은?"))
per_pay = int(input("시간당급여액은?"))

base_pay = work_time*per_pay
over_pay = 0

if work_time > 20:
    over_pay = (work_time -20)*per_pay/2
total_pay = base_pay + over_pay

print(f"{name} {work_time} {per_pay:.0f} {base_pay} {over_pay:.0f} {total_pay:.0f}")
"""
name = input("이름은?")
work_time = int(input("근무시간은?"))
hour_pay = int(input("시간당급여액은?"))

day_pay = work_time * hour_pay
over_pay = 0

if work_time > 20:
    over_pay = (work_time -20)*hour_pay/2
total_pay = day_pay + over_pay

print(f"{name}님의 초과근무 시간은 {work_time}시간으로 {hour_pay:,.0f} {day_pay:,.0f} {over_pay:,.0f} 총 급여액은 {total_pay:,.0f}")
    


## 컴퓨터활용능력시험
# 이름 필기(400) 워드(200) 스프레드시트(200) 프레젠테이션(200)
# 총점을 구하고 등급 800 이상 A, 800미만 600이상이 B, 600미만 400이상이 C, 400미만은 D, 재시험 요망

#입력: 이름, 필기, 워드, 스프레드시트, 프레젠테이션, 총점
#계산: A>=800, B < 800, 600< C, D<400

##강사님 풀이-----
#입력
# name = input("이름 : ")
# write = int(input("필기 : "))
# word = int(input("워드 : "))
# spread = int(input("스프레드시트 : "))
# ppt = int(input("프레젠테이션 : "))

# #계산
# total = write + word + spread + ppt
# if total >= 800:
#     grade = "A등급"
# elif total >= 600:
#     grade = "B등급"
# elif total >= 400:
#     grade = "C등급"
# else:
#     grade = "D등급, 재시험요망"

# print(f"{name} {write} {word} {spread} {ppt} {total} {grade}")




##나의 풀이-----
# name = input("이름은?")
# test = int(input("필기 점수는?"))
# word = int(input("워드 점수는?"))
# sheet = int(input("스프레드시트 점수는?"))
# pre = int(input("프레젠테이션 점수는?"))
# sum = test + word + sheet + pre

# if sum >= 800:
#     print(sum, "A")
# elif sum > 600:
#     print(sum, "B")
# elif sum > 400:
#     print(sum, "C")
# else:
#     print(f"{sum} D 재시험 요망")





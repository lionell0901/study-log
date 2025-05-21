# 지방 노동청에 신고가 들어옴 회사가 성별간 임금차별, 성별과 연봉이 들어온다.
# 직원 전체가 10명이고, 성별하고 연봉 입력 받아서 남자 평균, 여자 평균

#####강사님
worker_list = []
for i in range(0,10):
    gender = input("성별 : (M:남자 F:여자)")
    salary = int(input("연봉 : "))

    worker_list.append({"gender":gender}, {"salary":salary})

male_count=0

# pay_list = []
# gender_list = []
# male_list = []
# female_list = []
# maleavg_list = []
# femaleavg_list = []

# for i in range(4):
#     gender = input("성별 : ")
#     pay = int(input("연봉 : "))

#     if gender == "남":
#         male_list.append(pay)
#     else:
#         female_list.append(pay)
    
# if male_list:
#     maleavg_list = sum(male_list) / len(male_list)
# else:
#     maleavg_list = 0
# if female_list:
#     femaleavg_list = sum(female_list) / len(female_list)
# else:
#     femaleavg_list = 0

# print(f"남자 연봉 평균은 {maleavg_list:.0f} 여자 연봉 평균은 {femaleavg_list:.0f}입니다.")






"""
# # 나의 풀이 방법(챗GPT 참고)
# name_list = []
# korscore_list = []
# engscore_list = []
# mathscore_list = []
# avg_list = []
# total_list = []
# grade_list = []

# for i in range(0,3):
#     name = input("이름 : ")
#     korscore = int(input("국어점수 : "))
#     engscore = int(input("영어점수 : "))
#     mathscore = int(input("수학점수 : "))

#     name_list.append(name)
#     korscore_list.append(korscore)
#     engscore_list.append(engscore)
#     mathscore_list.append(mathscore)

# for i in range(0,3):
#     sum_score = korscore_list[i] + engscore_list[i] + mathscore_list[i]
#     total_list.append(sum_score)

# for i in range(0,3):
#     avg_score = (korscore_list[i] + engscore_list[i] + mathscore_list[i]) / 3
#     avg_list.append(avg_score)

# for i in range(0,3):
#     avg = avg_list[i]
#     if avg > 90:
#         grade = "수"
#     elif avg > 80:
#         grade = "우"
#     elif avg > 70:
#         grade = "미"
#     elif avg > 60:
#        grade = "양"
#     else:
#         grade = "가"
#     grade_list.append(grade)

# for i in range(0,3):
#     print(f"{name_list[i]}의 국어 점수는 {korscore_list[i]} 영어 점수는
     {engscore_list[i]} 수학 점수는 {mathscore_list[i]} 평균은 {avg_list[i]:.0f} 총점은 {total_list[i]} 학점은 {grade_list[i]}입니다.")
"""
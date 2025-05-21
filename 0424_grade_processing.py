print("Hello world")
# 이름, 국어, 영어, 수학 성적을 입력 받아 총점과 평균을 구하여 출력

#입력 : 이름(문자열), 국어, 영어, 수학 점수


student_name = input("이름?")
student_kor = int(input("국어?"))
student_eng = int(input("영어?"))
student_mat = int(input("수학?"))

#계산 - 수식 : 수학의 경우는 좌변과 우변을 바꿀 수 있다.
#   프로그램의 경우는 좌변은 언제나 변수만 가능하다.
student_total = student_kor + student_eng + student_mat
student_avg = student_total//3
#출력 : 총점과 평균
print(student_name, student_total, student_avg)

# 내가 한거 print(studen_name, "의 점수는" sum(student_kor, student_eng, student_mat), "입니다")
# 계산과 출력은 분리시키자(선생님 말씀)
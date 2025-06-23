
class ScoreData:
    def __init__(self, name = "홍길동", kor = 100, eng =100, mat =90):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.procee()
    
    def procee(self):
        self.total = self.kor + self.eng + self.mat
        self.avg = self.total / 3
        if self. avg >= 90:
            self.grade = "A"
        elif self.avg >= 80:
            self.grade = "B"
        elif self.avg >= 70:
            self.grade = "C"
        else:
            self.grade = "D, 재수강"

    def print(self):
        print(f'{self.name}', end = "\t")
        print(f'{self.kor}', end = "\t")
        print(f'{self.eng}', end = "\t")
        print(f'{self.mat}', end = "\t")
        print(f'{self.total}', end = "\t")
        print(f'{self.avg:.2f}', end = "\t")
        print(f'{self.grade}')
    
if __name__ == "__main__":
    s = ScoreData()
    s.print()

#학생들의 성적처리하는 프로그램
"""
class Student:
    def __init__(self, name, kor, eng, math): #학생 정보 생성자
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def getTotal(self): #과목 총점
        return self.kor + self.eng + self.math
    
    def getAverage(self): #과목 평균
        return self.getTotal() / 3
    
    def getGrade(self): #과목 등급
        if self.getAverage() >= 90:
            return "A"
        elif self.getAverage() >= 80:
            return "B"
        elif self.getAverage() >= 70:
            return "C"
        else:
            return "D, 재수강"
    def printLog(self): #학생 정보 출력
        print(f'이름 : {self.name}, 국어 : {self.kor}, 영어 : {self.eng}, 수학 : {self.math}', end = "\t")
        print(f'총점 : {self.getTotal()}, 평균 : {self.getAverage():.0f}, 등급 : {self.getGrade()}')
    
class StudentManager: #학생 관리 클래스 생성자

    def __init__(self): #학생 정보 리스트 생성자(바구니)
        self.students = []

    def addStudent(self, student): #학생 정보 추가
        self.students.append(student)

    def printAllStudents(self): #학생 정보 출력
        for student in self.students:
            student.printLog()
    
    def mainStart(self):
        while True:
            start = input("1. 학생정보 입력 2. 학생정보 출력 3. 종료")
            if start == "1":
                name = input("이름 : ")
                kor = int(input("국어 : "))
                eng = int(input("영어 : "))
                math = int(input("수학 : "))
                s = Student(name, kor, eng, math)
                self.addStudent(s)  # 학생 추가
            elif start == "2":
                self.printAllStudents()  # 학생 정보 출력
            elif start == "3":
                break
    

if __name__ == "__main__":
    sm = StudentManager()
    sm.mainStart()

"""

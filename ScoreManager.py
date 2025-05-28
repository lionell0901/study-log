from sqlalchemy import text
from ScoreData import ScoreData
from DBEngine import thEengine

class ScoreManager:
    def __init__(self):
        # 각 등급별 학생 수를 저장할 딕셔너리 초기화
        self.grade_summary = {'수': 0, '우': 0, '미': 0, '양': 0, '가': 0}
        self.scoreList = [] # scoreList도 여기서 초기화하는 것이 좋습니다.

    # 학생 목록을 가져오고, 개별 학생 정보를 출력한 뒤, 등급별 요약을 출력합니다.
    def output(self):
        sql = "select * from tb_score"
        # getList를 호출하여 self.scoreList를 채웁니다.
        self.getList(sql)

        if not self.scoreList:
            print("처리할 성적 데이터가 없습니다.")
            return

        print("\n[학생별 성적]")
        print("이름\t국어\t영어\t수학\t총점\t평균\t등급")
        print("----------------------------------------------------")
        for s in self.scoreList:
            s.output() # ScoreData 객체의 output 메서드 호출

        # 등급별 학생 수 계산을 위해 grade_summary 초기화
        self.grade_summary = {'수': 0, '우': 0, '미': 0, '양': 0, '가': 0}
        for s in self.scoreList:
            if s.grade in self.grade_summary: # 유효한 등급인지 확인
                self.grade_summary[s.grade] += 1
            # else: # 필요하다면 알 수 없는 등급에 대한 처리
                # print(f"알 수 없는 등급: {s.grade} 학생: {s.sname}")


        print("\n[등급별 인원수]")
        print("--------------------")
        for grade, count in self.grade_summary.items():
            print(f"{grade}: {count}명")
        print("--------------------")


    # 데이터베이스에서 성적 데이터를 가져와 self.scoreList에 ScoreData 객체로 저장합니다.
    def getList(self, sql):
        self.scoreList = [] # 새로운 데이터를 가져오기 전에 기존 목록을 비웁니다.
        with thEengine.begin() as conn:
            result = conn.execute(text(sql))
            for r in result.mappings().all():
                # ScoreData 생성 시 DB의 숫자 타입이 그대로 전달되도록 합니다.
                # ScoreData의 __init__에서 kor, eng, mat를 숫자로 처리해야 합니다.
                s = ScoreData(r["sname"], r["kor"],r["eng"],r["mat"])
                self.scoreList.append(s)


    # 새로운 성적 데이터를 사용자로부터 입력받아 데이터베이스에 삽입을 준비하는 과정을 처리합니다.
    def insertMain(self):
        # ScoreData 객체를 생성하여 입력받을 이름과 점수들을 임시로 저장합니다.
        # s = ScoreData() # ScoreData의 __init__이 점수들을 숫자로 받도록 수정되었다면, 여기서 초기화 방식 변경 고려
        sname = input("이름 : ")
        try:
            kor = int(input("국어 : ")) 
            eng = int(input("영어 : ")) 
            mat = int(input("수학 : ")) 
        except ValueError:
            print("점수는 숫자로 입력해야 합니다.")
            return

        # 데이터베이스에 성적을 삽입하기 위한 SQL 쿼리 문자열을 정의합니다.
        sql = """
        insert into tb_score(sname, kor, eng, mat)
        values(:sname, :kor, :eng, :mat)
        """

        # SQL 쿼리에 사용될 파라미터를 단일 딕셔너리 형태로 구성합니다.
        params = {"sname": sname, "kor": kor, "eng": eng, "mat": mat}
        # 실제로 데이터베이스에 삽입 작업을 수행하는 insert 메서드를 호출합니다.
        self.insert(sql, params)
        print(f"{sname} 학생의 성적이 입력되었습니다.")

    # 주어진 SQL 쿼리와 파라미터를 사용하여 데이터베이스에 데이터를 삽입합니다.
    def insert(self, sql, params):
        # thEengine.begin()을 사용하여 데이터베이스 연결 및 트랜잭션을 관리합니다.
        with thEengine.begin() as conn:
            # conn.execute(text(sql), params)를 통해 준비된 SQL 쿼리를 실행하여 데이터를 삽입합니다.
            conn.execute(text(sql), params)


# 이 스크립트가 직접 실행될 때의 기본 동작을 정의합니다.
if __name__ == "__main__":
    # ScoreManager의 인스턴스를 생성합니다.
    sm = ScoreManager()
    
    # 사용자에게 메뉴를 제공하여 기능을 선택할 수 있도록 합니다.
    while True:
        print("\n--- 성적 관리 프로그램 ---")
        print("1. 성적 입력")
        print("2. 전체 성적 출력 (등급별 인원 포함)")
        print("3. 종료")
        choice = input("원하는 작업의 번호를 입력하세요: ")

        if choice == '1':
            sm.insertMain()
        elif choice == '2':
            sm.output()
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
# SQLAlchemy 라이브러리에서 text 함수를 가져옵니다.
# 이 함수는 일반 텍스트 SQL 쿼리를 SQLAlchemy가 이해할 수 있는 형태로 변환하는 데 사용됩니다.
from sqlalchemy import text
# DBEngine 모듈에서 thEengine 객체를 가져옵니다.
# 이 객체는 데이터베이스 연결 엔진을 나타내는 것으로 보입니다.
from DBEngine import thEengine


#orm을 사용할때는 클래스를 만들어놓고 쓰는것이 맞음
class ScoreData:
    #db에서 레코드셋
    def __init__(self, sname="", kor=0, eng=0, mat=0):
        self.sname = sname
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.process()
    
    def output(self):
        print(f'{self.sname}',end="\t")
        print(f'{self.kor}',end="\t")
        print(f'{self.eng}',end="\t")
        print(f'{self.total}',end="\t")
        print(f'{self.average}', end="\t")
        print(f'{self.grade}')
    
    def process(self):
        self.total = self.kor+self.eng+self.mat
        self.average = self.total/3
        if self.average >=90:
            self.grade = "수"
        elif self.average >=80:
            self.grade = "우"
        elif self.average >=70:
            self.grade = "미"
        elif self.average >=60:
            self.grade = "양"
        else:
            self.grade = "가"


# 이 스크립트가 직접 실행될 때만 아래 코드를 실행하도록 합니다.
# 모듈로 가져와서 사용할 때는 실행되지 않습니다.
if __name__ == "__main__":
    # 데이터베이스 엔진을 사용하여 연결을 시작하고, conn이라는 이름으로 연결 객체를 가져옵니다.
    # with 문을 사용하여 작업이 끝나면 연결이 자동으로 닫히도록 합니다.
    with thEengine.begin() as conn:
        # emp 테이블의 모든 데이터를 선택하는 SQL 쿼리를 문자열로 정의합니다.
        sql= "select * from tb_score"
        # 정의된 SQL 쿼리를 데이터베이스 연결을 통해 실행하고, 그 결과를 result 변수에 저장합니다.
        # text() 함수를 사용하여 문자열 쿼리를 SQLAlchemy가 실행할 수 있는 형태로 만듭니다.
        result = conn.execute(text(sql))
        # 쿼리 실행 결과의 모든 행을 가져와서 콘솔에 출력합니다.
        for r in result.mappings().all():
            s = ScoreData(r["sname"], r["kor"],r["eng"],r["mat"])
            s.output()
           
import pymysql

# Database 클래스 정의
class Database:
    def __init__(self):
        # 데이터베이스에 연결
        self.db = pymysql.connect(
        host = 'localhost',  # 데이터베이스 호스트 주소
        user = 'user03',     # 데이터베이스 사용자 이름
        password = '1234',   # 데이터베이스 비밀번호
        db = 'project1',     # 데이터베이스 이름
        port = 3306)         # 데이터베이스 포트 번호
                             # 3306은 MySQL의 기본 포트 번호
                             # 1~65535 범위의 포트 번호 사용 가능
                             # 1~1000은 시스템 예약 포트
                             # 80은 HTTP(웹 서버) 포트

        # 커서를 생성하여 데이터베이스 작업을 수행
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    # 데이터 삽입, 갱신, 삭제를 위한 메서드
    # query: 실행할 SQL 쿼리
    # args: 쿼리에 전달할 인자, 기본값은 빈 튜플
    # 예: execute("INSERT INTO table_name VALUES (%s, %s)", (value1, value2))
    def execute(self, query, args=()):
        # 전달된 인자 출력
        print(args)
        # 쿼리 실행
        self.cursor.execute(query, args)
        # 변경사항 커밋
        self.db.commit()
    
    # 데이터 딱 한개만 가져오기
    # query: 실행할 SQL 쿼리
    # args: 쿼리에 전달할 인자, 기본값은 빈 튜플
    # 반환값: 쿼리 결과의 첫 번째 행
    def executeOne(self, query, args=()):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()  # 첫 번째 행 가져오기
        return row
    
    # 데이터 여러개 가져오기
    # query: 실행할 SQL 쿼리
    # args: 쿼리에 전달할 인자, 기본값은 빈 튜플
    # 반환값: 쿼리 결과의 모든 행
    def executeALL(self, query, args=()):
        self.cursor.execute(query, args)
        rows = self.cursor.fetchall()  # 모든 행 가져오기
        return rows
    
    # 데이터베이스 연결을 닫는 메서드
    # 데이터베이스가 열려 있는 경우에만 닫습니다.
    def close(self):
        if self.db.open:  # 데이터베이스가 열려 있는지 확인
            self.db.close()  # 데이터베이스 연결 닫기

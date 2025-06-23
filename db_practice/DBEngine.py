from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# 데이터베이스 연결 설정을 위한 라이브러리 임포트

# 데이터베이스 연결 엔진 생성
# mysql+pymysql://사용자이름:비밀번호@호스트주소:포트/데이터베이스이름
thEengine = create_engine(
    "mysql+pymysql://root:1234@localhost:3306/mydb",  # 접속할 데이터베이스 정보
    pool_size=10,        # 동시에 사용할 수 있는 최대 데이터베이스 연결 수
    max_overflow=5,      # pool_size를 초과할 때 추가로 만들 수 있는 연결 수
    pool_recycle=3600    # 연결을 재사용하기 전에 대기하는 시간(초) - 1시간 (MySQL 기본 타임아웃 8시간보다 짧게 설정하여 연결 오류 방지)
)

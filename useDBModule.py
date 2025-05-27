# DBModule에서 Database 클래스를 가져옴
from DBModule import Database

# 회원 목록을 출력하는 함수
def output():
    # Database 클래스의 인스턴스 생성 (데이터베이스에 연결)
    db = Database()
    # 실행할 SQL 쿼리 정의 (tb_member 테이블의 모든 데이터 조회)
    sql = "select * from tb_member"
    # SQL 쿼리를 실행하여 모든 결과 행을 가져옴
    rows = db.executeALL(sql)
    # 각 결과 행을 반복하여 출력
    for row in rows:
        print(row)  # 각 행의 데이터를 출력

    # 데이터베이스 연결 닫기 (리소스 정리)
    db.close()  

# 아이디 중복체크 -> 아이디 입력받고 나서 DB에 이미 존재하는지 체크하고
# 이미 존재하는 아이디입니다 하고 함수 종료
# 사용가능한 아이디입니다. 출력하고 나머지 입력받아 회원가입

# 단계 1: 아이디 중복체크 함수 (간단한 버전)
def check_id_exists(user_id):
    # 1단계: 데이터베이스 연결
    db = Database()
    
    # 2단계: SQL 쿼리 만들기 (해당 아이디가 있는지 찾기)
    sql = "select user_id from tb_member where user_id = %s"
    
    # 3단계: 쿼리 실행해서 결과 가져오기
    result = db.executeOne(sql, (user_id,))
    
    # 4단계: 데이터베이스 연결 끊기
    db.close()
    
    # 5단계: 결과 판단하기
    if result == None:  # 결과가 없으면 (None이면)
        return False    # 사용 가능한 아이디
    else:               # 결과가 있으면 
        return True     # 이미 존재하는 아이디
    
# #강사님 풀이법
# def idcheck(user_id=""):
#     if user_id == "" or user_id=="test": #에러체크
#         return False # 사용불가
    
#     sql = "select count(*) cnt from tb_member where user_id=%s"
#     db = Database()
#     row = db.executeOne(sql, (user_id))
#     cnt = row["cnt"]
#     db.close()
#     if row["cnt"]==0:
#         return True
#     return False

# 단계 2: 중복체크를 포함한 회원가입 함수
def member_register_with_check():
    print("=== 회원가입 ===")
    
    # 아이디 입력받고 중복체크 하기
    user_id = input("사용할 아이디를 입력하세요: ")
    
    #if not idcheck(user_id):
        # print("이미 사용중인 아이디입니다")
        # return
    # print("사용가능한 아이디입니다.")
    
    # 중복체크 실행
    if check_id_exists(user_id) == True:
        print("죄송합니다. 이미 존재하는 아이디입니다.")
        print("다시 시도해주세요.")
        return  # 함수 종료 (회원가입 중단)
    else:
        print("좋습니다! 사용 가능한 아이디입니다.")
    
    # 나머지 정보 입력받기
    password = input("패스워드: ")
    user_name = input("이름: ")
    email = input("이메일: ")
    phone = input("전화번호: ")
    
    # 데이터베이스에 저장하기
    db = Database()
    sql = """
        insert into tb_member(user_id, password, user_name, email, phone, regdate) 
        values(%s, %s, %s, %s, %s, now())
    """
    db.execute(sql, (user_id, password, user_name, email, phone))
    db.close()
    
    print("축하합니다! 회원가입이 완료되었습니다!")

if __name__ == "__main__":
    member_register_with_check()
    output()
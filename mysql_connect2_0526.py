import pymysql

# conn = pymysql.connect(
#     host = 'localhost',
#     user = 'user02',
#     password = 'qwer1234',
#     db = 'mydb',
#     port = 3306)


# cursor = conn.cursor(pymysql.cursors.DictCursor)
# ename ="조승연"
# sql = "select * from emp where ename='"+ename+"'"
# print(sql)
# cursor.execute(sql)
# rows = cursor.fetchall()
# print("데이터개수", len(rows))
# for row in rows:
#     print(row["empno"],row["ename"],row["sal"])


# #insert 는?
# sql = """
#     insert into emp(empno, ename, sal)
#     values(%s,%s,%s)

# """
def connect_db(): # DB와 연결고리. def connect_db()
    return pymysql.connect( #DB정보값 넣어주기(host, user 등등)
        host='localhost',
        user='root',
        password='1234',
        db='mydb',
        port=3306,
        charset='utf8mb4'
    )


def insert_score(conn):
    cursor = conn.cursor()
    sname = input("이름: ")
    kor = int(input("국어: "))
    eng = int(input("영어: "))
    mat = int(input("수학: "))

    sql = """
    INSERT INTO tb_score (sname, kor, eng, mat, regdate)
    VALUES (%s, %s, %s, %s, NOW())
    """
    cursor.execute(sql, (sname, kor, eng, mat))
    conn.commit()
    print("✅ 성적이 추가되었습니다.")

def fetch_all_scores(conn):
    cursor = conn.cursor()
    sql = """
    SELECT sname, kor, eng, mat, regdate
    FROM tb_score
    """
    cursor.execute(sql)
    return cursor.fetchall()

def print_scores(rows):
    print("\n📋 학생 성적 목록:")
    for row in rows:
        sname, kor, eng, mat, regdate = row
        total = kor + eng + mat
        avg = round(total / 3, 1)
        print(f"{sname} | 국어:{kor}, 영어:{eng}, 수학:{mat} | 총점:{total}, 평균:{avg} | 등록일:{regdate}")

def main():
    conn = connect_db()

    while True:
        print("\n[메뉴] 1. 성적 추가  2. 전체 조회  0. 종료")
        menu = input("선택: ")
        if menu == '1':
            insert_score(conn)
        elif menu == '2':
            rows = fetch_all_scores(conn)
            print_scores(rows)
        elif menu == '0':
            break
        else:
            print("❗ 올바른 메뉴를 선택하세요.")

    conn.close()
    print("🔚 프로그램 종료")

# 프로그램 실행
if __name__ == "__main__":
    main()
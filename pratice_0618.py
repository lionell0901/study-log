# 예제1 - 학생 데이터 정렬 예제
students = [  # 학생 정보를 담은 딕셔너리 리스트 생성
    {"name": "Alice", "score": 85, "age": 20},  # Alice 학생 정보
    {"name": "Bob", "score": 92, "age": 22},    # Bob 학생 정보
    {"name": "Charlie", "score": 92, "age": 19}, # Charlie 학생 정보
    {"name": "David", "score": 78, "age": 21}   # David 학생 정보
]

# sorted() 함수로 점수는 내림차순(-), 나이는 오름차순으로 정렬
sorted_students = sorted(students, key=lambda s: (-s["score"], s["age"]))

# 정렬된 학생 리스트를 반복하여 출력
for student in sorted_students:
    print(f"{student['name']} - Score: {student['score']}, Age: {student['age']}")

# 예제2 - pandas를 이용한 데이터 분석 기본 예제
import pandas as pd  # pandas 라이브러리 임포트
print(pd.__version__)  # pandas 버전 확인 및 출력

# 샘플 데이터를 딕셔너리 형태로 생성
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Lio"],  # 이름 컬럼
    "age": [25, 32, 40, 29, 50],  # 나이 컬럼
    "purchase": [120.5, 80.0, 230.0, 99.9, 100.0]  # 구매금액 컬럼
}
df = pd.DataFrame(data)  # 딕셔너리를 DataFrame으로 변환

print("---① 데이터 구조 확인---")  # 첫 번째 분석: 데이터 구조 파악
print("🔹 head():")  # head() 메서드 설명
print(df.head())  # 데이터의 처음 5행 출력
print("🔹 shape:", df.shape)  # 데이터의 행과 열 개수 출력
print("🔹 columns:", df.columns)  # 컬럼명 리스트 출력(열)
print("🔹 index:", df.index) # 데이터의 행 이름(행))

print("---② 요약 정보 확인---")  # 두 번째 분석: 데이터 요약 정보
print("🔹 info():")  # info() 메서드 설명
print(df.info())  # 데이터의 기본 정보(데이터 타입, 메모리 사용량 등) 출력
print("🔹 describe():")  # describe() 메서드 설명
print(df.describe())  # 수치형 데이터의 기술통계량(평균, 표준편차 등) 출력

print("---③ 결측값 확인---")  # 세 번째 분석: 결측값 검사
print("🔹 결측값:")  # 결측값 확인 설명
print(df.isnull().sum())  # 각 컬럼별 결측값 개수 출력

print("---④ 고유값 파악---")  # 네 번째 분석: 고유값 분포
print("🔹 age 분포:")  # name 컬럼의 고유값 분포 확인 (실제로는 name 컬럼)
print(df["name"].value_counts())  # name 컬럼의 값별 빈도수 출력

# 예제3
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
    "gender": ["F", "M", "M", "M", "F", "M", "F"],
    "age": [25, 32, 40, 22, 29, 35, 24]
}

df = pd.DataFrame(data)

# 성별별 고객 수 세기
gender_counts = df["gender"].value_counts()

# 나이별 고객 수 세기
age_counts =df["age"].value_counts()

# 나이 내림차순 정렬
sorted_df = df.sort_values(by="age", ascending=False)

print("🔹 성별별 고객 수:")
print(gender_counts)

print("🔹 나이별 고객 수:")
print(age_counts)

print("\n🔹 나이 많은 순:")
print(sorted_df[["name", "age"]])

# 예제4

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
    "gender": ["F", "M", "M", "M", "F", "M", "F"],
    "age": [25, 32, 40, 22, 29, 35, 24],
    "purchase": [120.5, 80.0, 230.0, 99.9, 150.0, 300.0, 180.0]
}

df = pd.DataFrame(data)
print(df.head())
print(df.shape)
print(df.describe())
print(df.index)
print(df.columns)
print(df.isnull().sum())

# 성별 그룹별 평균 계산
grouped = df.groupby("gender")[["age", "purchase"]].mean()

print(grouped)


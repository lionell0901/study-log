# 예제1
import pandas as pd
import numpy as np

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "purchase": [120.5, 80.0, 230.0, 99.9, 150.0]
}
df = pd.DataFrame(data)
# 구매 금액 기준으로 등급 부여
df["grade"] = df["purchase"].apply(lambda x: "VIP" if x >= 200 else "Regular")
print(df)

player ={
    "name": ["Lio", "Messil", "Ronaldo", "Pirlo", "Zidane"],
    "grade": [150, 200, 210, 180, 220]
} #축구 플레이어의 이름과 점수
df = pd.DataFrame(player) #player 데이터프레임 df 변수로 정의
df["class"] = df["grade"].apply(lambda x:"S" if x >= 200 else "A")
#class 칼럼에 grade 칼럼을 기준으로 만약 200보다 크거나 같으면 S등급, 그게 아니라면 A등급
print(df) #df 출력

# 예제2

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, np.nan, 40, 22, np.nan],
    "purchase": [120.5, 80.0, np.nan, 99.9, 150.0]
}

df = pd.DataFrame(data)

# 1. 결측값 확인
print("🔍 결측값 개수:")
print(df.isnull().sum())

# 2. 평균으로 age 결측값 채우기
df["age"] = df["age"].fillna(df["age"].mean())

# 3. purchase 컬럼에서 결측값 제거
df = df.dropna(subset=["purchase"])

print("\n✅ 정제 후 데이터:")
print(df)

# 예제3
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Lio"],
    "gender": ["F", np.nan, "M", "M", np.nan, "F", "M"],
    "purchase": [120.5, 80.0, 230.0, 99.9, 150.0, None, None]
}

df = pd.DataFrame(data)
print(df.isnull().sum())

print("gender 열을 최빈값으로 채우기")
df["gender_mode"] = df["gender"].fillna(df["gender"].mode()[0])

# 2. purchase 열은 "결측"을 명시적으로 표현
df["purchase_status"] = df["purchase"].fillna("결측")

print(df)

# 예제4
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "gender": ["F", "M", "M", "M", "F"]
}

df = pd.DataFrame(data)

# 1. map을 사용해 gender 열을 한글로 바꾸기
df["gender_kor"] = df["gender"].map({"F": "여성", "M": "남성"})

# 2. replace로 name 열에서 특정 이름 변경
df["name_fixed"] = df["name"].replace({"Charlie": "찰리", "David": "데이비드", "Alice":"앨리스"})

print(df)

# 예제5
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "membership": ["Gold", "Silver", "Bronze", "Silver", "Gold"]
}

df = pd.DataFrame(data)

# 멤버십을 원-핫 인코딩으로 변환
dummies = pd.get_dummies(df["membership"])

# 기존 df에 붙이기
df_encoded = pd.concat([df, dummies], axis=1)

print("--dummies 예시--")
print(dummies)
print("--df_encoded 예시--")
print(df_encoded)

# 예제6
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 샘플 데이터
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Lio"],
    "age": [25, 32, 41, 29, 35, 38, 27],
    "gender": ["F", "M", "M", "M", "F", "F", "M"],
    "purchase": [120.5, 80.0, 230.0, 99.9, 150.0, 250.0, 180.0],
    "VIP": [0, 0, 1, 0, 0, 1, 1]  # 예측할 대상: VIP 여부
}

df = pd.DataFrame(data)

df = pd.get_dummies(df, columns=["gender"], drop_first=True)  # 'M' 여부만 표시
X = df[["age", "purchase", "gender_M"]]  # 입력값 (X)
y = df["VIP"]                            # 출력값 (y)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("정확도:", accuracy_score(y_test, y_pred))
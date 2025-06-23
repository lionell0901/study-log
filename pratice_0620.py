# 예제1
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# 샘플 데이터
data = {
    "age": [25, 32, 41, 29, 35, 38, 27],
    "purchase": [120.5, 80.0, 230.0, 99.9, 150.0, 250.0, 180.0],
    "gender": ["F", "M", "M", "M", "F", "F", "M"],
    "VIP": [0, 0, 1, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

# 데이터 확인(결측지, 정보 등)
print(df.isnull().sum())
print(df.info)
print(df.head())
print(df.describe())

# # 범주형 처리
df = pd.get_dummies(df, columns=["gender"], drop_first=True)

# # X, y 나누기
X = df[["age", "purchase", "gender_M"]]
y = df["VIP"]

# # 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# # 1️⃣ 정규화 (StandardScaler 적용: 평균 0, 표준편차 1)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # test는 transform만!

# # 2️⃣ 모델 훈련 & 평가
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

print("정확도:", accuracy_score(y_test, y_pred))

# 예제2
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# 데이터
data = {
    "age": [25, 32, 41, 29, 35, 38, 27],
    "purchase": [120.5, 80.0, 230.0, 99.9, 150.0, 250.0, 180.0],
    "gender": ["F", "M", "M", "M", "F", "F", "M"],
    "VIP": [0, 0, 1, 0, 0, 1, 1]
}
df = pd.DataFrame(data)

# 인코딩
df = pd.get_dummies(df, columns=["gender"], drop_first=True)

# 변수 분리
X = df[["age", "purchase", "gender_M"]]
y = df["VIP"]

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 정규화
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 모델 학습
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# 1️⃣ VIP 여부 예측
print("예측 결과 (VIP 여부):", model.predict(X_test_scaled))

# 2️⃣ VIP 확률 예측
print("예측 확률 (VIP일 확률):")
print(model.predict_proba(X_test_scaled))  # [[0.8 0.2], [0.3 0.7] ...]


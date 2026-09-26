import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. 데이터 로드
df = pd.read_csv("WA_FnUseC_TelcoCustomerChurn.csv")

# 2. 학습에 쓰지 않을 컬럼 제거
df = df.drop(columns=["customerID"])

# 3. TotalCharges 숫자형 변환
# 공백이나 잘못된 값은 NaN으로 변환
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# 4. 입력(X)과 타깃(y) 분리
X = df.drop(columns=["Churn"])
y = df["Churn"]

# 5. 수치형 / 범주형 컬럼 구분
numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns
categorical_cols = X.select_dtypes(include=["object"]).columns

print("수치형 컬럼:")
print(numeric_cols.tolist())

print("\n범주형 컬럼:")
print(categorical_cols.tolist())

# 6. 수치형 전처리
# 결측치는 중앙값으로 채우고, StandardScaler로 스케일링
numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]
)

# 7. 모델 학습
# Logistic Regression 모델 추가
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced",  # 클래스 불균형 고려
    random_state=42           # 재현성 설정
)
# 7. 범주형 전처리
# 결측치는 최빈값으로 채우고, One-Hot Encoding
categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ]
)

# 8. 수치형 / 범주형 전처리 결합
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_cols),
        ("cat", categorical_transformer, categorical_cols)
    ]
)

# 9. 전처리 + Logistic Regression Pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000))
    ]
)

# 10. 학습 / 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 11. 모델 학습
model.fit(X_train, y_train)

# Random Forest도 같은 분할을 사용하며 독립된 전처리 객체를 학습한다.
rf_model = Pipeline(steps=[
    ("preprocessor", clone(preprocessor)),
    ("classifier", RandomForestClassifier(
        n_estimators=200,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1,
    )),
])
rf_model.fit(X_train, y_train)

# 12. 평가
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print("[Logistic Regression]")
print(f"Accuracy: {acc:.4f}")
rf_pred = rf_model.predict(X_test)
print("[Random Forest]")
print(f"Accuracy: {accuracy_score(y_test, rf_pred):.4f}")

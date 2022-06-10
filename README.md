# **빅데이터분석기사 실기 연습**

모든 문제 출처 : https://www.kaggle.com/datasets/agileteam/bigdatacertificationkr


- ### 결측치 확인
```python
print(df.isnull().sum())
```

- ### 결측치 채우기
```python
df = df.fillna(df['칼럼명'].mean()) # mean, median, min, max 등

# 뒤에 나오는 값으로 채우기
df = df.fillna(method='bfill') # 앞에 값으로 채우기 method=ffill
```

- ### 결측치 제거
```python
df = df.dropna(subset=['칼럼명']) # axis=0 or 1 -> 결측치가 있는 row, col을 drop
```

- ### Pandas DataFrame 정렬
```python
df = df.sort_values('칼럼명', ascending=True) # 내림차순: ascending=False
```

- ### 칼럼 삭제
```python
df = df.drop(['칼럼명'], axis=1)
```

- ### Min-Max Scale
```python
from sklearn.preprocessing import minmax_scale
df['칼럼명'] = minmax_scale(data['칼럼명'])
```

- ### IQR 구하기 (Q1, Q3)
```python
Q1 = df['칼럼명'].quantile(25)
Q3 = df['칼럼명'].quantile(75)
IQR = Q3 - Q1
# 이상치
x < Q1 - 1.5 * IQR
x > Q3 + 1.5 * IQR
```

- ### 왜도, 첨도 (skewness, kurtosis)
```python
skew = df['칼럼명'].skew() # 왜도
kurt = df['칼럼명'].kurt() # 첨도
```


note:
T1-19 시계열 데이터3 Expected Question 다시 풀기


## **2유형**
```python
# 라이브러리
# 데이터 불러오기
# EDA
# 데이터 전처리
# 피처 엔지니어링
# 모델링, 하이퍼파라미터 튜닝, 앙상블
# csv 
```

- ### Label Encoding (문자열 자료를 숫자로 바꿀때 활용 가능)
```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
cols = ['칼럼명1', '칼럼명2'] # 변경할 문자열 칼럼 명

for col in cols:
  X_train[col] = le.fit_transform(X_train[col])
  X_test[col] = le.fit_transform(X_test[col])
```

- ### Random Forest
```python
# 분류(Classifier)
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=10)
# Hyperparameter
1. n_estimators : Tree 개수 (default=100)
2. max_depth : 최대 깊이 (default=None)
3. randoma_state : 지정해줘야 매번 같은 결과 도출

model.fit(X_train, y_train['칼럼명']) # y_train에 id가 존재하는 경우 해당 칼럼을 학습 데이터에 넣지 않기 위해 칼럼 지정
print(model.score(X_train, y_train['칼럼명']))

pred = model.predict_proba(X_test)

# 회귀(Regressor)
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state=10)
model.fit(X_train, y_train['칼럼명'])
print(model.score(X_train, y_train['칼럼명']))

pred = model.predict_proba(X_test)
```

# **빅데이터분석기사 실기 연습**


### 결측치 확인
```python
print(df.isnull().sum())
```

### 결측치 채우기
```python
df = df.fillna(df['칼럼명'].mean()) # mean, median, min, max 등

# 뒤에 나오는 값으로 채우기
df = df.fillna(method='bfill') # 앞에 값으로 채우기 method=ffill
```

### 결측치 제거
```python
df = df.dropna(subset=['칼럼명']) # axis=0 or 1 -> 결측치가 있는 row, col을 drop
```

### Pandas DataFrame 정렬
```python
df = df.sort_values('칼럼명', ascending=True) # 내림차순: ascending=False
```

### 칼럼 삭제
```python
df = df.drop(['칼럼명'], axis=1)
```

### Min-Max Scale
```python
from sklearn.preprocessing import minmax_scale
df['칼럼명'] = minmax_scale(data['칼럼명'])
```

### IQR 구하기 (Q1, Q3)
```python
Q1 = df['칼럼명'].quantile(25)
Q3 = df['칼럼명'].quantile(75)
IQR = Q3 - Q1
# 이상치
x < Q1 - 1.5 * IQR
x > Q3 + 1.5 * IQR
```

### 왜도, 첨도 (skewness, kurtosis)
```python
skew = df['칼럼명'].skew() # 왜도
kurt = df['칼럼명'].kurt() # 첨도
```



note:
T1-19 시계열 데이터3 Expected Question 다시 풀기

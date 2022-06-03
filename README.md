# **빅데이터분석기사 실기 연습**

### 결측치 채우기
```python
a = a.fillna(a[칼럼명].mean()) # mean, median, min, max 등
```

### Pandas DataFrame 정렬
```python
df = df.sort_values('칼럼명', ascending=True) # 내림차순: ascending=False
```

# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
from sklearn.preprocessing import power_transform

df = pd.read_csv('data/basic1.csv')

df = df[df['age']>=20]
# 최빈값으로 'f1' 컬럼 결측치 대체
df['f1'] = df['f1'].fillna(df['f1'].mode()[0])
# 'f1'데이터 여-존슨 yeo-johnson 값 구하기
df['y'] = power_transform(df[['f1']],method='yeo-johnson')
# 'f1'데이터 박스-콕스 box-cox 값 구하기
df['b'] = power_transform(df[['f1']], method='box-cox')
# 두 값의 차이를 절대값으로 구한다음 모두 더해 소수점 둘째 자리까지 출력(반올림)
print(round(sum(abs(df['y']) - df['b']), 2))
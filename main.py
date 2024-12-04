import pandas as pd
from src.trimAddress import process_address
from src.getLotNumberAddress import get_lot_number_address

# Excel 파일 불러오기
file_path = "data/schools.xlsx"  # 파일 경로를 여기에 입력하세요
df = pd.read_excel(file_path)

# 주소 컬럼 전처리
df['도로명 주소'] = df['주소'].apply(process_address)

# 지번 주소 컬럼 추가
df['지번 주소'] = df['도로명 주소'].apply(get_lot_number_address)

# 결과 확인
print(df)

# 결과 저장
df.to_excel("data/schools_processed.xlsx", index=False)

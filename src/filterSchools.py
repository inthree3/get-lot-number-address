import pandas as pd

# Excel 파일 불러오기
file_path = "data/schools_processed.xlsx"  # 원본 파일 경로
output_file_path = "data/eui_schools.xlsx"  # 저장할 파일 경로

# 데이터를 불러옵니다
df = pd.read_excel(file_path)

# 필터링할 동 이름 목록
target_areas = ['영등포본동', '영등포동', '여의동', '당산동', '도림동', '문래동', '양평동', '신길동', '대림동']

# 주소 컬럼에서 필터링 (예: '주소' 컬럼)
filtered_df = df[df['지번 주소'].str.contains('|'.join(target_areas), na=False)]

# 결과를 Excel로 저장
filtered_df.to_excel(output_file_path, index=False)

print(f"필터링된 데이터가 '{output_file_path}'에 저장되었습니다.")

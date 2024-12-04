import pandas as pd

# Excel 파일 불러오기
file_path = "data/schools_processed.xlsx"  # 원본 파일 경로
output_file_path = "data/eul_schools.xlsx"  # 저장할 파일 경로

# 데이터를 불러옵니다
df = pd.read_excel(file_path)

# 필터링할 동 이름 목록
target_areas = ['']

# 정확히 일치하는 단어만 찾기 위한 정규식 패턴 생성
# 각 단어를 \b (단어 경계)로 감싸서 정확히 일치하도록 함
regex_pattern = r'\b(' + '|'.join(target_areas) + r')\b'

# 주소 컬럼에서 필터링 (예: '주소' 컬럼)
filtered_df = df[df['지번 주소'].str.contains(regex_pattern, na=False)]

# 결과를 Excel로 저장
filtered_df.to_excel(output_file_path, index=False)

print(f"필터링된 데이터가 '{output_file_path}'에 저장되었습니다.")

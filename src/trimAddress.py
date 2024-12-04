import pandas as pd

# Excel 파일 불러오기
file_path = "../data/schools.xlsx"  # 파일 경로를 여기에 입력하세요
df = pd.read_excel(file_path)

# 주소 컬럼 전처리
def process_address(address):
    import re
    # '서울특별시'로 시작하고 뒤에 숫자와 (-숫자)가 붙는 패턴 추출
    match = re.search(r'서울특별시\s([^,]+)\s(\d+(?:-\d+)?)', address)
    if match:
        return f"서울특별시 {match.group(1)} {match.group(2)}"  # 서울특별시를 포함한 주소 반환
    else:
        return None  # 매칭되지 않는 경우 None 반환

df['도로명 주소'] = df['주소'].apply(process_address)

# 결과 저장
df.to_excel("data/schools_processed.xlsx", index=False)


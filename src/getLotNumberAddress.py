import requests
from bs4 import BeautifulSoup

def get_lot_number_address(roadNameAddress: str) -> str:
    urlBase = "https://www.juso.go.kr/support/AddressMainSearch.do?searchKeyword="
    roadNameAddress = roadNameAddress.replace(" ", "+")
    try:
        # URL에 GET 요청 보내기
        response = requests.get(urlBase + roadNameAddress)
        response.raise_for_status()  # HTTP 오류가 있는 경우 예외 발생

        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 클래스가 'mark type_2'인 요소 선택
        mark_element = soup.select_one('.mark.type_2')
        
        if mark_element and mark_element.find_next_sibling():
            # 다음 형제 요소의 텍스트 가져오기
            lot_address = mark_element.find_next_sibling().get_text(strip=True)
            
            # 탭과 줄바꿈 제거
            result_address = lot_address.replace('\t', '').replace('\n', '')

            # 결과 출력
            if result_address:
                return result_address
            else:
                raise ValueError("일치하는 결과가 없습니다.")
        else:
            raise ValueError("일치하는 결과가 없습니다.")
    except Exception as e:
        return f"에러 발생: {e}"

# 함수 사용 예시
query = "서울특별시 영등포구 의사당대로 1"
print(get_lot_number_address(query))
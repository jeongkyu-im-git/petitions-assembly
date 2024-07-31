# Copilot chat
# 
# 파이썬으로 크롤링 결과를 csv 파일로 저장하는 코드를 만들꺼야. 
# 다음 조건을 만족해줘
# - 요청 URL : https://petitions.assembly.go.kr/api/petits?pageIndex=1&recordCountPerPage=10000&sort=AGRE_CO-&searchCondition=sj&searchKeyword=&petitRealmCode=&sttusCode=PETIT_FORMATN,CMIT_FRWRD,PETIT_END&resultCode=BFE_OTHBC_WTHDRAW,PROGRS_WTHDRAW,PETIT_UNACPT,APPRVL_END_DSUSE,ETC_TRNSF&notInColumn=RESULT_CODE&beginDate=20200101&endDate=20240731&ageCd=
# - User-Agent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
# - CSV 파일명 : extracted-crawling-petitions-assembly-list.csv
# 
# 크롤링 정보 조회
# 목록 조회 Query (1400건)
# https://petitions.assembly.go.kr/api/petits?pageIndex=1&recordCountPerPage=10000&sort=AGRE_CO-&searchCondition=sj&searchKeyword=&petitRealmCode=&sttusCode=PETIT_FORMATN,CMIT_FRWRD,PETIT_END&resultCode=BFE_OTHBC_WTHDRAW,PROGRS_WTHDRAW,PETIT_UNACPT,APPRVL_END_DSUSE,ETC_TRNSF&notInColumn=RESULT_CODE&beginDate=20200101&endDate=20240731&ageCd=
# 
# 상세 조회 Query 
# https://petitions.assembly.go.kr/api/petits/14CBAF8CE5733410E064B49691C1987F?petitId=14CBAF8CE5733410E064B49691C1987F&sttusCode= 
#
# pip install requests pandas
# 

import requests
import pandas as pd

# API URL
url = 'https://petitions.assembly.go.kr/api/petits?pageIndex=1&recordCountPerPage=10000&sort=AGRE_CO-&searchCondition=sj&searchKeyword=&petitRealmCode=&sttusCode=PETIT_FORMATN,CMIT_FRWRD,PETIT_END&resultCode=BFE_OTHBC_WTHDRAW,PROGRS_WTHDRAW,PETIT_UNACPT,APPRVL_END_DSUSE,ETC_TRNSF&notInColumn=RESULT_CODE&beginDate=20200101&endDate=20240731&ageCd='

# 요청 헤더에 User-Agent 추가
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

# API 요청
response = requests.get(url, headers=headers)
response.raise_for_status()  # 요청이 성공했는지 확인

# JSON 데이터 파싱
data = response.json()

# 필요한 데이터 추출
# petitions = data['list']
petitions = data

# DataFrame으로 변환
df = pd.DataFrame(petitions)

# CSV 파일로 저장
csv_path = 'extracted-crawling-petitions-assembly-list.csv'
df.to_csv(csv_path, index=False, encoding='utf-8-sig')

print(f'CSV 파일이 생성되었습니다: {csv_path}')

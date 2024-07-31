# 원본 csv 파일에서 추출된 컬럼을 데이터 매핑하여 새로운 csv 파일을 만드는 파이썬 코드를 만드는데 아래 조건을 만족해야해.

# - 원본 CSV : extracted-crawling-petitions-assembly-list.csv
# - 타겟 CSV : petitions-assembly-dataset.csv
# - 추출 컬럼 : rowNum,petitRealmNm, petitSj, petitCn, agreCo, agreBeginDe, agreEndDe
# - 데이터 매핑(원본 컬럼명 : 타켓 컬럼명)
# rowNum : rowno
# petitRealmNm:catetory
# petitSj:title
# petitCn:content
# agreCo:count
# agreBeginDe:start
# agreEndDe:end
# - 날짜는 yyyy-mm-dd 형태로 저장


import pandas as pd

# 원본 CSV 파일 경로
input_file = 'extracted-crawling-petitions-assembly-list.csv'
# 타겟 CSV 파일 경로
output_file = 'petitions-assembly-dataset.csv'

# 추출할 열 목록 및 매핑
columns_to_extract = {
    'rowNum': 'rowno',
    'petitRealmNm': 'category',
    'petitSj': 'title',
    'petitCn': 'content',
    'agreCo': 'count',
    'agreBeginDe': 'start',
    'agreEndDe': 'end'
}

# CSV 파일 읽기
df = pd.read_csv(input_file)

# 특정 열만 추출하고 열 이름 변경
df_extracted = df[list(columns_to_extract.keys())].rename(columns=columns_to_extract)

# 날짜 형식 변환
df_extracted['start'] = pd.to_datetime(df_extracted['start']).dt.strftime('%Y-%m-%d')
df_extracted['end'] = pd.to_datetime(df_extracted['end']).dt.strftime('%Y-%m-%d')

# 새로운 CSV 파일로 저장
df_extracted.to_csv(output_file, index=False)

print(f"추출된 데이터가 {output_file}에 저장되었습니다.")

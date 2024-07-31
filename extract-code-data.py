# Copilot chat
# 
# extracted-crawling-petitions-assembly-list.csv 파일을 읽어서 코드 데이터만 추출해서 extracted-code-data.csv 파일을 만드는 파이썬 코드를 만들꺼야. 
# 코드 데이터를 만드는 조건은 다음과 같아.
# 
# - 결과 csv layout은 3개의 컬럼(Group name, Code, Name)으로 구성.
# - 결과 csv 컬럼의 헤더 타입은 text, 사이즈는 255 byte.
# - 대상 CSV에서 코드 데이터 쌍은 다음과 같고, 결과 csv layout의 Code , Name 값에 셋팅
# petitRealmCode : petitRealmNm
# petitRealmDetailCode : petitRealmDetailNm
# jrsdCmitCode : jrsdCmitNm
# sttusCode : sttusCodeNm
# resultCode : resultCodeNm
# jdgmnStepCode : jdgmnStepCodeNm
# petitUnacptCode : petitUnacptCodeNm
# - 결과 csv의 Group name 은 대상 CSV에서 Code로 끝나는 헤더명을 셋팅.
# - 결과 csv에서 Group Name, Code, Name은 중복 될 수 없음.
# - 결과 csv를 생성할 때 Group Name, Code, Name 오름차순으로 정렬.

import pandas as pd

# 원본 CSV 파일 읽기
df = pd.read_csv('extracted-crawling-petitions-assembly-list.csv')

# 코드 데이터 쌍 정의
code_pairs = {
    'petitRealmCode': 'petitRealmNm',
    'petitRealmDetailCode': 'petitRealmDetailNm',
    'jrsdCmitCode': 'jrsdCmitNm',
    'sttusCode': 'sttusCodeNm',
    'resultCode': 'resultCodeNm',
    'jdgmnStepCode': 'jdgmnStepCodeNm',
    'petitUnacptCode': 'petitUnacptCodeNm'
}

# 결과를 저장할 리스트 초기화
result = []

# 코드 데이터 추출
for code, name in code_pairs.items():
    if code in df.columns and name in df.columns:
        group_name = code
        for idx, row in df.iterrows():
            result.append([group_name, row[code], row[name]])

# DataFrame으로 변환
result_df = pd.DataFrame(result, columns=['Group name', 'Code', 'Name'])

# 중복 제거
result_df.drop_duplicates(inplace=True)

# 오름차순 정렬
result_df.sort_values(by=['Group name', 'Code', 'Name'], inplace=True)

# 결과 CSV 파일로 저장
result_df.to_csv('extracted-code-data.csv', index=False, header=True)

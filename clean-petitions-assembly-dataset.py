# Copilot chat
# 
# 원본 CSV 파일에서 아래 규칙을 적용하여 대상 CSV 파일로 저장하는 파이썬 코드를 만들어줘.
# 
# - 원본 CSV 파일 : petitions-assembly-dataset.csv
# - 대상 CSV 파일 : petitions-assembly-dataset-clean.csv
# - title, content 컬럼에 대해서 정규식을 적용
# - 모든 문자에서 엔터와 탭을 공백으로 치환.
# - 모든 특수 문자를 제거.(단, 콤마, 마침표는 제외)

import pandas as pd
import re

# 원본 CSV 파일 경로
input_file = 'petitions-assembly-dataset.csv'
# 대상 CSV 파일 경로
output_file = 'petitions-assembly-dataset-clean.csv'

# CSV 파일 읽기
df = pd.read_csv(input_file)

# 엔터, 탭을 공백으로 치환하고, 특수 문자를 제거하는 함수 (콤마와 마침표는 제외)
def clean_text(text):
    # 엔터와 탭을 공백으로 치환
    text = re.sub(r'[\n\t]', ' ', str(text))
    # 특수 문자를 제거 (콤마와 마침표는 제외)
    text = re.sub(r'[^A-Za-z0-9가-힣,\. ]', '', text)
    return text

# 대상 컬럼 목록
target_columns = ['title', 'content']

# 대상 컬럼에 대해 엔터, 탭 및 특수 문자 제거 적용
for column in target_columns:
    df[column] = df[column].apply(clean_text)

# 새로운 CSV 파일로 저장
df.to_csv(output_file, index=False)

print(f"정리된 데이터가 {output_file}에 저장되었습니다.")

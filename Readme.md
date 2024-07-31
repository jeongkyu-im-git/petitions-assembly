# Project Title

국민 청원 분류 하기

본 프로젝트는 AI 핵심 기술 집중 클래스(160 시간) 에 대한 미니 프로젝트입니다.

## Getting Started

로컬 환경으로만 구성되어 있습니다.

### Installing

크롤링과 데이터셋 구성을 위해 다음 모듈 설치 필요함.

```
pip install requests pandas
```

## Running the tests

```
# Create list csv file.
python crawling-petitions-assembly-list.py

# Output filename : extracted-crawling-petitions-assembly-list.csv


# Create code csv file.
python extract-code-data.py 

# Output filename : extracted-code-data.csv


# Create dataset for project
python create-petitions-assembly-dataset.py

# Output filename : petitions-assembly-dataset.csv
```

## Data layout

크롤링 추출 데이터에서 프로젝트에 필요한 타겟 데이터 구성

|항목명|원본 영문명|타켓 영문명|타입|데이터 포멧|비고|
|------|---|---|--|--|--|
|글번호|rowNum|rowno|Number|||
|카테고리|petitRealmNm|category|Text|||
|청원제목|petitSj|title|Text|||
|청원내용|petitCn|content|Text|||
|참여인원|agreCo|count|Number|||
|청원 시작일|agreBeginDe|start|Timestamp|%Y-%m-%d||
|청원 마감일|agreEndDe|end|Timestamp|%Y-%m-%d||

````
# dataset for project
convert_dataset = ['rowNum','category', 'title', 'content', 'count', 'start', 'end']
````
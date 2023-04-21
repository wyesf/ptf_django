
import os
import django
import csv
import sys



# 용산 / 중구 / 종로 / 영등포 / 서초

# 일반 파이썬앱(스크립트)에서 django ORM을 사용하려면 다음의 설정 필요
# django 환경설정 파일 지정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wys_django_ptf.settings")
# django settings 메모리 로딩 적용
django.setup()

from dashboard.models import Opexseoul

CSV_PATH='./dashboard/datas/data_last/yeongdeungpo/yeongdeungpo.csv'

with open(CSV_PATH, 'r',  encoding='utf-8') as file: 
  data_rows = csv.reader(file) 

  # print(data_rows)
  # print(list(data_rows))
  
  # 데이터 처리
  for row in data_rows : 
    # print(row) 

    if row[2].isdigit() :
      # print(row)

      row[3] = row[3].replace(',','')
      # print(row[1])

      if "스타벅스" not in row[1] and "투썸" not in row[1] and "할리스" not in row[1] and "폴바셋" not in row[1] and "정관장" not in row[1] and "파리크라상" not in row[1] and "마트" not in row[1] and "이디야" not in row[1] and "커피" not in row[1] and "맘스터치" not in row[1] and "카페" not in row[1] :
        # print(row)

        Opexseoul.objects.create( 
          
          regDate = row[0],
          restaurant = row[1],
          personnel = row[2],
          price = row[3],
          borough = '영등포구'

        )

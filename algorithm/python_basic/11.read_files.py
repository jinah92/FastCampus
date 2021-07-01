# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# ex 1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) Header 스킵

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ => 반복문 실행 가능

    for c in reader:
        print(c)

# ex 2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')   # delimiter : 구분자로 열 분리 (구분자 콤마가 아닌 경우)
    # next(reader) Header 스킵

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ => 반복문 실행 가능

    for c in reader:
        print(c)

# ex 3 (dict 변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('---------')

# ex 4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv', 'w', newline='') as f:
    # newline='' => 줄바꿈 버림
    wt = csv.writer(f)
    
    for v in w:
        wt.writerow(v)

# ex 5
with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w) # writerows => 한번에 쓰기


# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(openpyxl, xlrd를 내부적으로 사용)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# sheetname = '시트명' 또는 숫자, header=숫자, skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인 (default : 5)
print(xlsx.head())

# 데이터 확인   (default : 5)
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape) # 행, 열

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=True)
xlsx.to_csv('./resource/result.csv', index=True)

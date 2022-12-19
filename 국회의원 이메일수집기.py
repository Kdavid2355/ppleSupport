import requests
import pprint
import pandas as pd
import json
import openpyxl

#OpenAPI 인증키를 활용해 데이터 가져오기
url = "https://open.assembly.go.kr/portal/openapi/---------인증키주소--------&TYPE=json&pIndex=1&pSize=300"
response = requests.get(url)
contents = response.text

#필요한 데이터만 가져오기
dump = json.loads(contents)
raw_data = dump['nwvrqwxyaytdsfvhu'][1]['row']

#데이터프레임 만들기
count = 1
df_final = pd.DataFrame(columns=['순번','성함','정당','방법','소속위원회','이메일','사무실번호'])

#데이터프레임에 데이터 집어넣기
for x in raw_data:
    df_plus = {'순번' : count, '성함': x['HG_NM'], '정당': x['POLY_NM'],'방법': x['ELECT_GBN_NM'],'소속위원회' : x['CMITS'],'이메일': x['E_MAIL'], '사무실번호': x['TEL_NO']}
    df_final = df_final.append(df_plus, ignore_index=True)
    count += 1

print(df_final)

#엑셀 파일 출력
df_final.to_excel("Assembly_email.xlsx", sheet_name="국회의원 현황자료")

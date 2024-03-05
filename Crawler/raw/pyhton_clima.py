import csv
import requests
import gzip

CSV_URL="https://portal.inmet.gov.br/uploads/dadoshistoricos/2021.zip"

with requests.Session() as s:
    download = s.get(CSV_URL)
    with open('2021.zip','wb') as f:
        f.write(download.content)
    
f = gzip.open('INMET_S_RS_A801_PORTO ALEGRE_01-01-2021_A_31-12-2021.CSV', 'rt')
file_content=f.read()

cr = csv.reader(file_content.splitlines(), delimiter=',')
my_list = list(cr)
for row in my_list:
    print(row)


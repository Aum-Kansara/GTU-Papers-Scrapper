import requests
import os
from zipfile import ZipFile

years=["W2022","W2021","W2020","W2019","W2018","W2017","S2023","S2023","S2022","S2021","S2020","S2019","S2018"]

subject_codes=["3170701","2170701"]
courses=["AF","BA","BB","BC","BD","BE","BESP","BH","BI","BL","BM","BN","BP","BPSP","BT","BV","CS","DA","DB","DH","DI","DISP","DM","DP","DS","DV","EP","FD","HM","IB","IC","IM","MA","MB","MC","MCSP","MD","ME","MH","ML","MN","MP","MR","MS","MT","MV","PB","PD","PH","PM","PP","PR","TE"]

save_folder_path=r"D:\ITM\Sem 6\Information Extraction Workshop\Project\Project\static\Compiler Design"

course=courses[5]
os.chdir(save_folder_path)
for year in years:
    for subject_code in subject_codes:
        url=f"https://www.gtu.ac.in/uploads/{year}/{course}/{subject_code}.pdf"
        res=requests.get(url)
        if subject_code not in os.listdir():
            os.mkdir(subject_code)
        if res.status_code==200:
            summer_or_winter="SUMMER" if year[0]=='S' else "WINTER"
            paper_year=year[1:]
            filename=f"{subject_code}-{course}-{summer_or_winter}-{paper_year}.pdf"
            with open(subject_code+'/'+filename,"wb") as f:
                f.write(res.content)
            print("Downloaded",filename)
        else:
            print("Not Found")

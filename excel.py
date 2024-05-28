# -*- coding: utf-8 -*-
import pandas as pd

all_name = ['評價','食物類型','店家資訊','地理位置','食物價位']
rename = ['Comment','Type','Info','Position','Price']

# Read the Excel file
for i,name in enumerate(all_name):
    df = pd.read_excel('database_eng.xlsx',sheet_name=name)
    df.to_excel(rename[i]+'.xlsx', index=False)

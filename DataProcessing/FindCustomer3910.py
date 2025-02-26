import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import re

def search_google(company_name):
    """產生 Google 搜尋連結，而不自動爬取結果"""
    return f"https://www.google.com/search?q={company_name}"

def clean_data(input_file, output_file, keywords, hs_codes, shipping_codes, shipper):
    df = pd.read_excel(input_file)
    
    condition = df['产品描述'].str.contains('|'.join(keywords), case=False, na=False) | \
                df['装运标志及编号'].astype(str).str.contains('|'.join(shipping_codes), na=False) | \
                df['产品海关编码'].astype(str).str.contains('|'.join(hs_codes), na=False) | \
                df['发货人'].str.contains('|'.join(shipper), case=False, na=False)

    filtered_df = df[condition].copy()
    filtered_df['公司网站'] = filtered_df['收货人'].apply(search_google)
    
    filtered_df.to_excel(output_file, index=False, engine='openpyxl')
    print(f'篩選並查找聯繫方式完成，結果儲存至 {output_file}')

def process_all_files(input_folder, output_folder, keywords, hs_codes, shipping_codes,shipper):
    os.makedirs(output_folder, exist_ok=True)
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".xlsx"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name.replace("New", "Final_"))
            print(f'處理文件: {file_name}')
            clean_data(input_path, output_path, keywords, hs_codes, shipping_codes,shipper)

keywords = ['3910' , 'silicone fluid', 'silicone rubber', 'silicone oil', 'silicone polyether' ]
hs_codes = ['3910']
shipping_codes = ['3910']
shipper = ['etsu', 'MOMENTIVE','Wacker','dow','Elkem']

input_folder = '/Users/chinghaochang/silicone 數據/美國 silicone year excel'
output_folder = '/Users/chinghaochang/silicone 數據/美國 silicone year fina excel'
process_all_files(input_folder, output_folder, keywords, hs_codes, shipping_codes, shipper)

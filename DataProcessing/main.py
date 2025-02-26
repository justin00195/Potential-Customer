from fastapi import FastAPI, Query
import pandas as pd
import numpy as np
import os

app = FastAPI()

file_path = "/Users/chinghaochang/silicone 數據/英文版/English2023 silicone.xlsx"
df = pd.read_excel(file_path)

# 定義API首頁




@app.get("/filter")
def filter_data(
    column: str = Query(..., description="請輸入要篩選的欄位名稱"),
    keywords: str = Query(..., description="請輸入篩選關鍵字 以逗號分隔")
):
    if column not in df.columns:
        return {"error": f"欄位 '{column}' 不存在，請選擇有效的欄位。"}
    
    df[column] = df[column].astype(str).str.lower()

    keywords_list  = [kw.strip().lower() for kw in keywords.split(",") if kw.strip()]


    if keywords_list:
        filter_condition = df[column].str.contains("|".join(keywords_list), na=False)
        filtered_df = df[filter_condition]
    else:
        return {"error": "請輸入至少一個有效的關鍵字"}
    
    filtered_df = filtered_df.replace({np.nan: None, np.inf: None, -np.inf: None})

    return filtered_df.head(1000).to_dict(orient="records")


    

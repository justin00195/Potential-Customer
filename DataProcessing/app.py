import streamlit as st
import pandas as pd
import requests
import io

# FastAPI 伺服器的 URL
API_URL = "http://127.0.0.1:8000/filter"

# 設定標題
st.title("進出口查詢系統")

# 設定可選篩選欄位
columns = ["Product_Description", "HS_Code", "Importer"]
select_columns = st.selectbox("選擇篩選欄位", columns)

# 使用者輸入關鍵字
keywords = st.text_input("輸入關鍵字（可輸入多個，逗號分隔）", "")

# 每頁顯示 10 筆
page_size = 10

# 初始化 session_state
if "page_number" not in st.session_state:
    st.session_state.page_number = 1
if "data" not in st.session_state:
    st.session_state.data = []
if "total_pages" not in st.session_state:
    st.session_state.total_pages = 1

# 按鈕觸發 API 請求
if st.button("開始篩選"):
    if keywords:
        # 發送 API 請求
        formatted_keywords = ",".join([kw.strip() for kw in keywords.split(",") if kw.strip()])
        params = {"column": select_columns, "keywords": formatted_keywords}
        response = requests.get(API_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            total_results = len(data)

            if total_results > 0:
                # 計算總頁數
                total_pages = (total_results // page_size) + (1 if total_results % page_size > 0 else 0)

                # 更新 session_state
                st.session_state.data = data
                st.session_state.total_pages = total_pages
                st.session_state.page_number = 1  # 重設到第一頁

            else:
                st.warning("No data for your keyword")
        else:
            st.error(f"API 發生錯誤：{response.status_code}")
    else: 
        st.warning("Please enter a keyword")

# 建立上一頁 & 下一頁按鈕

# **顯示當前頁面的數據**
if st.session_state.data:
    start_idx = (st.session_state.page_number - 1) * page_size
    end_idx = start_idx + page_size
    df = pd.DataFrame(st.session_state.data[start_idx:end_idx])
    st.dataframe(df)

    # 顯示頁碼
    st.write(f"第 {st.session_state.page_number} 頁 / 共 {st.session_state.total_pages} 頁")


col1, col2 = st.columns([1, 1])

with col1:
    if st.button("上一頁"):
        if st.session_state.page_number > 1:
            st.session_state.page_number -= 1

with col2:
    if st.button("下一頁"):
        if st.session_state.page_number < st.session_state.total_pages:
            st.session_state.page_number += 1 


if st.button("下載篩選結果"):
    if st.session_state.data:
        df_download = pd.DataFrame(st.session_state.data)
        output = io.BytesIO()
        df_download.to_excel(output, index=False)
        output.seek(0)

        st.download_button(
            label="📥 下載 Excel",
            data=output,
            file_name="filtered_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    else: 
         st.warning("⚠️ 沒有數據可下載")

         

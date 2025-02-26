import pandas as pd
import os

file_path = '/Users/chinghaochang/silicone 數據/英文版/English2023 silicone.xlsx'
df = pd.read_excel(file_path)

df["Product_Description"] = df["Product_Description"].astype(str).str.lower()
df["HS_Code"] = df["HS_Code"].astype(str)


user_input = input("Enter keywords, separate by , :" ).strip().lower()
keywords = []
for kw in user_input.split(","):
    if kw.strip():
        keywords.append(kw.strip())

#keywords = [kw.strip() for kw in user_input.split(",") if kw.strip()]

# 產生篩選條件
keywords_filter = df["Product_Description"].apply(lambda desc: any(kw in desc for kw in keywords))
hscode_filter = df["HS_Code"].apply(lambda hscode: any(hscode.startswith(kw) for kw in keywords))

filtered_df = df[keywords_filter | hscode_filter]


print(filtered_df.head(10))

save_dir = "/Users/chinghaochang/silicone 數據/Filteredtest"
save_name = "Filtered2023 silicone.xlsx"
save_path = os.path.join(save_dir, save_name)

filtered_df.to_excel(save_path, index=False)
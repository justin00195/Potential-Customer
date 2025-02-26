import os
import pandas as pd

def CleanDataCsv(input_file, output_file):

    df = pd.read_excel(input_file)

    print("原始欄位:", df.columns)
    df.columns = df.columns.str.strip()

    colmns_to_drop = [ 'CIF总值(消费)','散装货CIF千克单价' , '散装货CIF总值', '散装货FOB千克单价', '散装货FOB总值']
    df.drop(columns = [col for col in colmns_to_drop if col in df.columns], inplace = True)

    df.to_csv(output_file, index= False, encoding= 'utf-8-sig')
    print(f'數據清理完畢，以儲存csv{output_file}')

def CleanDataExcel(input_file, output_file):

    df = pd.read_excel(input_file, engine='openpyxl', keep_default_na=False)

    print("原始欄位:", df.columns)
    df.columns = df.columns.str.strip()

    colmns_to_drop = ['CIF总值(消费)','散装货CIF千克单价' , '散装货CIF总值', '散装货FOB千克单价', '散装货FOB总值']
    df.drop(columns = [col for col in colmns_to_drop if col in df.columns], inplace = True)

    df.to_excel(output_file, index=False, engine='openpyxl')
    print(f'數據清理完畢，以儲存csv{output_file}')

def ProcessingFile(input_folder, output_folder, output_folderexcel):

        os.makedirs(output_folder, exist_ok=True)
        os.makedirs(output_folderexcel, exist_ok=True)

        for file_name in os.listdir(input_folder):
            if file_name.endswith(".xlsx"):
                input_path = os.path.join(input_folder, file_name)
                output_path = os.path.join(output_folder, file_name.replace(".xlsx", ".csv"))
                output_excelpath = os.path.join(output_folderexcel, file_name.replace("202", "New202"))
                print(f'處理文件：{file_name}')
                CleanDataCsv(input_path, output_path)
                CleanDataExcel(input_path, output_excelpath)


input_folder = '/Users/chinghaochang/silicone 數據/美國 3910000'
output_folder = '/Users/chinghaochang/silicone 數據/美國 3910000 clean_data'
output_folderexcel = '/Users/chinghaochang/silicone 數據/美國 3910000 clean_dataExcel'

ProcessingFile(input_folder, output_folder,output_folderexcel)
import pandas as pd
import os

def clean_data(input_file, output_file):
    df = pd.read_excel(input_file)

    print("原始欄位:", df.columns)
    df.columns = df.columns.str.strip()

    df.drop_duplicates(inplace=True)

    colmns_to_drop = ['船东提单号' , '货代提单号', '航次', '提单当前状态', 'MBL4' , 'HBL4','货代提单类型','首次录入AMS系统时间','SITC1','SITC2','SITC3','SITC4','SITC']
    df.drop(columns = [col for col in colmns_to_drop if col in df.columns], inplace = True)

    df.replace("", pd.NA, inplace=True)
    print("填補前缺失值:\n", df.isnull().sum())
    

    df.fillna({
        '产品描述': 'None',
        '收货人': 'None',
        '发货人': 'None',
        '数量': 0,
        '原产国': 'None',
        '发货人地址' :  'None',
        '通知人' :  'None',
        '承运人' :  'None',
        '原产国' :  'None',
        '海外装货港':  'None',
        '目的港':  'None',
        '目的国' :  'None',
        '启运国':  'None',
        '货运收货人' : 'None',
        '收货人所在州' : 'None',
        '产品海关编码' : 00000000,
        '尺寸' : 0*0*0
    }, inplace=True)

    print("填補後缺失值:\n", df.isnull().sum())
    

    df.to_csv(output_file, index= False, encoding= 'utf-8-sig')
    print(f'數據清理完畢，以儲存csv{output_file}')

def clean_dataexcel(input_file, output_file):

    
    df = pd.read_excel(input_file, engine='openpyxl', keep_default_na=False)

    print("原始欄位:", df.columns)
    df.columns = df.columns.str.strip()

    df.drop_duplicates(inplace=True)

    colmns_to_drop = ['船东提单号' , '货代提单号', '航次', '提单当前状态', 'MBL4' , 'HBL4','货代提单类型','首次录入AMS系统时间','SITC1','SITC2','SITC3','SITC4','SITC']
    df.drop(columns = [col for col in colmns_to_drop if col in df.columns], inplace = True)

    df.replace("", pd.NA, inplace=True)
    print("填補前缺失值:\n", df.isnull().sum())

    #刪除重複值？
    

    df.fillna({
        '产品描述': 'None',
        '收货人': 'None',
        '发货人': 'None',
        '数量': 0,
        '原产国': 'None',
        '发货人地址' :  'None',
        '通知人' :  'None',
        '承运人' :  'None',
        '原产国' :  'None',
        '海外装货港':  'None',
        '目的港':  'None',
        '目的国' :  'None',
        '启运国':  'None',
        '货运收货人' : 'None',
        '收货人所在州' : 'None',
        '产品海关编码' : 00000000,
        '尺寸' : 0*0*0
    }, inplace=True)

    print("填補後缺失值:\n", df.isnull().sum())
    

    df.to_excel(output_file, index=False, engine='openpyxl')
    print(f'數據清理完畢，以儲存excel{output_file}')


def ProcessingFile(input_folder, output_folder):

        os.makedirs(output_folder, exist_ok=True)

        for file_name in os.listdir(input_folder):
            if file_name.endswith(".xlsx"):
                input_path = os.path.join(input_folder, file_name)
                output_path = os.path.join(output_folder, file_name.replace(".xlsx", ".csv"))
                print(f'處理文件：{file_name}')
                clean_data(input_path, output_path)

def ProcessingFileExcel(input_folder, output_folderexcel):

        os.makedirs(output_folderexcel, exist_ok=True)

        for file_name in os.listdir(input_folder):
            if file_name.endswith(".xlsx"):
                input_path = os.path.join(input_folder, file_name)
                output_path = os.path.join(output_folderexcel, file_name.replace("202", "New202"))
                print(f'處理文件：{file_name}')
                clean_dataexcel(input_path, output_path)

input_folder = '/Users/chinghaochang/silicone 數據/美國 silicone year'
output_folder = '/Users/chinghaochang/silicone 數據/美國 silicone year csv'
output_folderexcel = '/Users/chinghaochang/silicone 數據/美國 silicone year excel'

ProcessingFile(input_folder, output_folder)
ProcessingFileExcel(input_folder, output_folderexcel)

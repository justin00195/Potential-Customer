import pandas as pd
import os
df = pd.read_excel('/Users/chinghaochang/silicone 數據/美國 silicone year fina excel/Final_2023 美國silicone.xlsx')

df.rename(columns={
    "实际抵达日期": "Arrival_Date",
    "产品描述": "Product_Description",
    "收货人": "Importer",
    "收货人地址": "Importer_Address",
    "发货人": "Exporter",
    "发货人地址": "Exporter_Address",
    "通知人": "Notify_Party",
    "承运人": "Carrier",
    "原产国": "Country_of_Origin",
    "海外装货港": "Overseas_Loading_Port",
    "目的港": "Destination_Port",
    "目的国": "Destination_Country",
    "启运国": "Shipping_Country",
    "产品件数/拼箱货柜": "Product_Units",
    "数量单位": "Quantity_Unit",
    "TEU": "TEU",
    "千克重/拼箱货柜": "Weight_Per_Container",
    "千克重/件": "Weight_Per_Unit",
    "尺寸": "Size",
    "货运收货人": "Freight_Consignee",
    "货柜号": "Container_Number",
    "卸货港": "Unloading_Port",
    "卸货港所在州": "Unloading_State",
    "装运标志及编号": "Shipping_Marks_and_Numbers",
    "产品海关编码": "HS_Code",
    "货柜运输类型": "Container_Transport_Type",
    "支线承运人收货地": "Feeder_Carrier_Receiving_Location",
    "货运托运人": "Freight_Shipper",
    "双抬头托运人": "Dual_Shipper",
    "货柜个数/船东提单": "Number_of_Containers",
    "收货人所在州": "Importer_State"
}, inplace = True)


save_dir = "/Users/chinghaochang/silicone 數據/英文版"
save_filename = "English2023 silicone.xlsx"
save_path = os.path.join(save_dir, save_filename)
df.to_excel(save_path, index=False)
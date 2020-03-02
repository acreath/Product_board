import pandas as pd

#将csv数据转为dataframe
csv_file = "data.csv"
csv_data = pd.read_csv(csv_file, low_memory=False) # 防止弹出警告
csv_df = pd.DataFrame(csv_data)
print(csv_df)
print(csv_df.shape) # 查看行数和列数
print(csv_df.info()) # 查看总体情况
print(csv_df.head()) # 输出前5行
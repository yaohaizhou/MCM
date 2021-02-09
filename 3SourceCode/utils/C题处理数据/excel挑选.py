import pandas as pd

xlsx = pd.read_excel("test.xlsx") #打开文件
data_head = list(xlsx.columns)
num_col = len(data_head)

data = xlsx.values
rows = len(xlsx)
columns = len(xlsx.head())
output = []

for i in range(rows):
    if data[i][2] >= 1970:      # 2是选中某一列的元素对齐进行条件筛选
        output.append(data[i])
dataframe = pd.DataFrame(
     output, columns=data_head
)
print(dataframe)
dataframe.to_excel("result.xlsx",sheet_name=">=1970")       
# 第一个参数写明输出的文件；
# 第二个参数写明表单的名字                                                                    
import numpy as np
import pandas as pd

def TOPSIS(A:pd.DataFrame):
    """
    :param A: (n,m) n个对象,m个指标构成的Dataframe对象
    :return: 返回权重最终向量
    """
    # 1.正向化的矩阵A(输入时需要完成)
    # 2.转换为无量纲数据，便于多个指标综合考虑
    values = A.values/np.sqrt(np.sum(A.values**2,axis=0))
    # 3.标准化
    max_val = np.max(values,axis=0)
    min_val = np.min(values,axis=0)
    min_vals = np.sqrt(np.sum((values-min_val)**2,axis=1))
    max_vals = np.sqrt(np.sum((max_val-values)**2,axis=1))
    values = min_vals/(max_vals+min_vals)
    # 4.归一化
    values = values/np.sum(values)
    return pd.DataFrame(data=values,columns=["综合得分"],index=A.index)


A = pd.DataFrame([
    [89,1],
    [60,3],
    [74,2],
    [99,0]
],columns=['成绩','争吵次数'],index=['小明','小王','小张','清风'])

result = TOPSIS(A)
print(result)
# values = A.values

# print(values/np.sqrt(np.sum(values**2,axis=0)))
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class AHP:
    def __init__(self,A:pd.DataFrame,RI = [0,0,0.58,0.90,1.12,1.24,1.32,1.41,1.45,1.49,1.51]):
        """
        :param A: 判断矩阵组成的DF(index=columns)
        :param RI: 随机一致性检验RI的标准值
        """
        self.RI = RI
        self.A = A

        # 确认A为正互反矩阵
        assert self.assert_(), "判断矩阵不是正互反矩阵，请重新确认"

    # 判断A是否为正互反矩阵
    def assert_(self):
        matrix = self.A.values
        for i in range(len(matrix)):
            for j in range(i):
                if matrix[i,j] != 1/matrix[j,i]:
                    return False
        return True

    # 平均法计算权重
    def weight_mean(self):
        mean = np.mean(self.A.values,axis=0)
        return mean/np.sum(mean)

    # 特征向量法计算权重
    def weight_eig(self):
        eigvals,eigvecs = np.linalg.eig(self.A.values)
        return np.abs(eigvecs[:,0]/np.sum(np.abs(eigvecs[:,0])))

    # 计算层内的一致性检验指标
    def CI(self):
        eigvals,_ = np.linalg.eig(self.A.values)
        n = len(self.A.values)
        return (eigvals[0]-n)/(n-1)

    # 计算一致性比率CR
    def CR(self,CI):
        n = len(self.A)
        try:
            CR = CI/self.RI[n-1]
        except ZeroDivisionError:
            print("除数为0出现错误")
        return CR

def ahp(A:pd.DataFrame):
    """
    :param A: 判断矩阵组成的DF(index=columns)
    """
    print(A)
    ahp1 = AHP(A)
    eigvecs = ahp1.weight_eig()
    print("Weight by eigvectors:",eigvecs)
    mean_weights = ahp1.weight_mean()
    print("Weight by mean:",mean_weights)
    CI = ahp1.CI()
    print("CI:",CI)
    CR = ahp1.CR(CI)
    print("CR:",CR)

df = pd.DataFrame([
    [1,1/2,4,3,3],
    [2,1,7,5,5],
    [1/4,1/7,1,1/2,1/3],
    [1/3,1/5,2,1,1],
    [1/3,1/5,3,1,1]
],index = ["景色","费用","居住","饮食","旅途"],
columns = ["景色","费用","居住","饮食","旅途"])

ahp(df)

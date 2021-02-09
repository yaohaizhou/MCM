import numpy as np
import math
"""
GM(1,1)模型适合具有较强的指数规律的数列，只能描述其单调的变化过程，适合少数据预测。
流程：
    1.对原始数据进行级比检验，满足则进行，不满足则退出进行平移变换
    2. 做累加生成(1-AGO)序列
    3. 生成邻值生成序列
    4. 建立GM(1,1)的灰微分方程模型，得到此微分方程的解析解
    5. 建立灰色微分方程的白化方程，得到白化方程的解析解
    6. 还原累减获得预测序列
    7. 进行预测值的检验
"""
class GM:
    def __init__(self,X:np.ndarray):
        self.X = X
        # 对原始数据进行级比检验
        assert self._assert(self.X),"数据级比不满足要求，请先行处理数据"
        self.a = None
        self.b = None

    def _grade_ratio(self,X: np.ndarray):
        # 级比
        lambda_k = np.array([X[k - 1] / X[k] for k in range(1, len(X))])
        return lambda_k
    # 级比检验
    def _assert(self, X: np.ndarray):
        lambda_k = self._grade_ratio(X)
        # 级比的上下界
        lower = math.exp(-2 / (len(X) + 1))
        upper = math.exp(2 / (len(X) + 1))
        lambda_k = (lambda_k < upper) * (lambda_k > -lower)
        if np.sum(lambda_k) == len(lambda_k):
            return True
        else:
            return False

    # 对数据做累加
    def _increasing(self,X):
        aggregate_result = []
        sum = 0
        for k in range(len(X)):
            sum += X[k]
            aggregate_result.append(sum)
        return np.array(aggregate_result)

    # 均值生成序列
    def _mean_generating_series(self,X:np.ndarray,alpha = 0.5):
        return -np.array([alpha*X[k]+(1-alpha)*X[k+1] for k in range(len(X)-1)])

    # 解灰微分方程得到解析解
    def _solve_grayeq(self,X:np.ndarray,Z:np.ndarray):
        B = np.vstack((Z,[1]*len(Z)))
        Y = X[1:]
        return np.linalg.inv(B.dot(B.T)).dot(B).dot(Y.reshape((len(Y),1)))
    
    # 解白微分方程得到解析解
    def _solve_whiteeq(self, X: np.ndarray, theta:np.ndarray):
        a,b = theta
        X_tilde = []
        for k in range(1,len(X)):
            X_tilde.append(float((X[0]-b/a)*math.exp(-a*k)+b/a))
        X_tilde.insert(0,X[0])
        return np.array(X_tilde)

    # 模型检验
    def _final_check(self,X_tilde):
        print("\n原始值:",self.X)
        print("模型值:",X_tilde)
        print("残差:",self.X-X_tilde)
        print("相对误差:",np.abs(self.X-X_tilde)/self.X*100)
        print("级比偏差:",self._decreasing(self._grade_ratio(X_tilde)))

    # 模型训练
    def fit(self):
        print("原始序列：",self.X)
        X = self._increasing(self.X)
        print("一次累加序列：",X)
        Z = self._mean_generating_series(X)
        print("一次均值生成序列:",Z)
        theta = self._solve_grayeq(self.X,Z)
        print("灰色模型参数:\na:",theta[0],"\tb:",theta[1])
        X_tilde = self._solve_whiteeq(self.X,theta)
        print("模型预测累加生成数列为：",X_tilde)
        X_tilde = self._decreasing(X_tilde)
        print("模型预测结果为:",X_tilde)
        self._final_check(X_tilde)
        self.a = theta[0]
        self.b = theta[1]

    # 后续的预测balabala
    def predict(self,X):
        pass

    # 对数据做累减
    def _decreasing(self,X:np.ndarray):
        X_tilde = [X[0]]
        for k in range(1,len(X)):
            X_tilde.append(X[k]-X[k-1])
        return np.array(X_tilde)



X = np.array([71.1,72.4,72.4,72.1,71.4,72.0,71.6])
gm = GM(X)
gm.fit()

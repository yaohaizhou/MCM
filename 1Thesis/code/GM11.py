import numpy as np
import math

class GM:
    def __init__(self,X:np.ndarray):
        self.X = X
        assert self._assert(self.X),""
        self.a = None
        self.b = None
    def _grade_ratio(self,X: np.ndarray):
        lambda_k = np.array([X[k - 1] / X[k] for k in range(1, len(X))])
        return lambda_k
    def _assert(self, X: np.ndarray):
        lambda_k = self._grade_ratio(X)
        lower = math.exp(-2 / (len(X) + 1))
        upper = math.exp(2 / (len(X) + 1))
        lambda_k = (lambda_k < upper) * (lambda_k > -lower)
        if np.sum(lambda_k) == len(lambda_k):
            return True
        else:
            return False
    def _increasing(self,X):
        aggregate_result = []
        sum = 0
        for k in range(len(X)):
            sum += X[k]
            aggregate_result.append(sum)
        return np.array(aggregate_result)
    def _decreasing(self,X:np.ndarray):
        X_tilde = [X[0]]
        for k in range(1,len(X)):
            X_tilde.append(X[k]-X[k-1])
        return np.array(X_tilde)
    def _mean_generating_series(self,X:np.ndarray,alpha = 0.5):
        return -np.array([alpha*X[k]+(1-alpha)*X[k+1] for k in range(len(X)-1)])
    def _solve_grayeq(self,X:np.ndarray,Z:np.ndarray):
        B = np.vstack((Z,[1]*len(Z)))
        Y = X[1:]
        return np.linalg.inv(B.dot(B.T)).dot(B).dot(Y.reshape((len(Y),1)))
    def _solve_whiteeq(self, X: np.ndarray, theta:np.ndarray):
        a,b = theta
        X_tilde = []
        for k in range(1,len(X)):
            X_tilde.append(float((X[0]-b/a)*math.exp(-a*k)+b/a))
        X_tilde.insert(0,X[0])
        return np.array(X_tilde)
    def _final_check(self,X_tilde):
        print("\noriginals:",self.X)
        print("model values:",X_tilde)
        print("residual:",self.X-X_tilde)
        print("relative error:",np.abs(self.X-X_tilde)/self.X*100)
        print("ratio error:",self._decreasing(self._grade_ratio(X_tilde)))
    def train(self):
        X = self._increasing(self.X)
        Z = self._mean_generating_series(X)
        theta = self._solve_grayeq(self.X,Z)
        X_tilde = self._solve_whiteeq(self.X,theta)
        X_tilde = self._decreasing(X_tilde)
        print("prediction result:",X_tilde)
        self._final_check(X_tilde)
        self.a = theta[0]
        self.b = theta[1]

X = np.array([52,51,51,51,50,50,50,50,52,51,50,51,54,51])
gm = GM(X)
gm.train()
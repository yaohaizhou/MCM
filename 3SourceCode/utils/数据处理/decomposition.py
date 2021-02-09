import numpy as np
# PCA无监督降维
from sklearn.decomposition import PCA
# LDA有监督降维
from sklearn.discriminant_analysis import LinearClassifierMixin
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

"""
1.PCA无监督降维
2.LDA有监督降维
"""
iris = load_iris()
X = np.array(iris.data)

pca = PCA(n_components=2)
result = pca.fit_transform(X)
plt.scatter(result[:50, 0], result[:50, 1], label="0")
plt.scatter(result[50:100, 0], result[50:100, 1], label="1")
plt.scatter(result[100:, 0], result[100:, 1], label="2")
plt.title("result of PCA")
plt.legend()
plt.show()
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from st_dbscan import ST_DBSCAN

df = pd.read_csv("2021MCMProblemC_DataSet.csv")
df['time'] = (pd.to_datetime(df['time'])-pd.to_datetime(df['time'].min())).map(lambda x:x.days)
data = df.loc[df['label']=="Positive ID", ['time','x','y']].values
st_dbscan = ST_DBSCAN(eps1 = 0.3, eps2 = 30, min_samples = 5) 
st_dbscan.fit(data)
def plot(data, labels):
    colors = ['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00','#cab2d6','#6a3d9a']
    for i in range(-1, len(set(labels))):
        if i == -1:
            col = [0, 0, 0, 1]
        else:
            col = colors[i % len(colors)]
        clust = data[np.where(labels==i)]
        plt.scatter(clust[:,0], clust[:,1], c=[col], s=5)
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.show()
    return None
plot(data[:,1:], st_dbscan.labels)

score = []
for i in range(len(st_dbscan.labels)):
    score.append(0)
    for component in st_dbscan.components:
        score[i]+=component[i]
    score[i] /= len(st_dbscan.labels)
    # score[i] = -score[i]
    score[i] = 1/score[i]
print(score)

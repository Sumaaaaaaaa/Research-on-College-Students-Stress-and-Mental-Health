import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 生成随机数据
data = np.random.rand(10, 12)

# 创建聚类热力图
sns.clustermap(data, cmap='viridis', metric='euclidean', method='ward')
plt.show()
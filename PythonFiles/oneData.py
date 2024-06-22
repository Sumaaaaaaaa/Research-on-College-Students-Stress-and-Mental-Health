import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# 参数
n = 9
p = 529 / 2958

# 创建 x 值范围
x = np.arange(0, n + 1)

# 计算 PMF
pmf = binom.pmf(x, n, p)

# 绘图
plt.figure(figsize=(12, 6))
plt.plot(x, pmf, 'bo', ms=2)
plt.vlines(x, 0, pmf, colors='b', lw=0.5)
plt.title('Binomial Distribution PMF (n=2958, p=529/2958)')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.grid(True)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

x_means = []
N = 10  # サンプルサイズ

for _ in range(10_000):
    xs = []
    for n in range(N):
        x = np.random.rand()  # 一様分布からの乱数
        xs.append(x)

    x_mean = np.mean(xs)
    x_means.append(x_mean)

# グラフの描画
plt.hist(x_means, bins="auto", density=True)
plt.title(f"N={N}")
plt.xlabel("x")
plt.ylabel("Probability Density")  # y軸は「確率密度」
plt.xlim(-0.05, 1.05)
plt.ylim(0, 5)
plt.show()

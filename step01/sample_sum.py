import numpy as np
import matplotlib.pyplot as plt

x_sums = []
N = 5

for _ in range(10_000):
    xs = []
    for n in range(N):
        x = np.random.rand()  # 一様分布からの乱数
        xs.append(x)
    t = np.sum(xs)  # 和を求める
    x_sums.append(t)


# 正規分布
def normal(x, mu: float = 0.0, sigma: float = 1.0):
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / np.sqrt(2 * np.pi * sigma**2)


x_norm = np.linspace(-5, 5, 1000)
mu = N / 2
sigma = np.sqrt(N / 12)
y_norm = normal(x_norm, mu, sigma)

# グラフの描画
plt.hist(x_sums, bins="auto", density=True)
plt.plot(x_norm, y_norm)
plt.title(f"N={N}")
plt.xlim(-1, 6)  # x軸の範囲を-1〜6の間に指定
plt.show()

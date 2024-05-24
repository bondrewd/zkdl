import numpy as np
import matplotlib.pyplot as plt


def normal(x, mu: float = 0.0, sigma: float = 1.0):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)


x = np.linspace(-10, 10, 1000)

y0 = normal(x, mu=-3)
y1 = normal(x, mu=0)
y2 = normal(x, mu=5)

plt.plot(x, y0, label=r"$\mu=-3$")
plt.plot(x, y1, label=r"$\mu=0$")
plt.plot(x, y2, label=r"$\mu=5$")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

y0 = normal(x, sigma=0.5)
y1 = normal(x, sigma=1.0)
y2 = normal(x, sigma=2.0)

plt.plot(x, y0, label=r"$\sigma=0.5$")
plt.plot(x, y1, label=r"$\sigma=1.0$")
plt.plot(x, y2, label=r"$\sigma=2.0$")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

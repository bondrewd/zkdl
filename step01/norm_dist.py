import numpy as np
import matplotlib.pyplot as plt


def normal(x, mu=0, sigma=1):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)


x = np.linspace(-5, 5, 100)
y = normal(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

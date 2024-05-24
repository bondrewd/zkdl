import pathlib
import numpy as np
import matplotlib.pyplot as plt

path = pathlib.Path(__file__).parent.joinpath("height.txt")
xs = np.loadtxt(path)

mu = np.mean(xs)
sigma = np.std(xs)


def normal(x, mu, sigma):
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / np.sqrt(2 * np.pi * sigma**2)


x = np.linspace(150, 190, 1_000)
y = normal(x, mu, sigma)


plt.hist(xs, bins="auto", density=True)
plt.plot(x, y)
plt.xlabel("Height (cm)")
plt.ylabel("Probability Density")
plt.show()

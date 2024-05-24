import pathlib
import numpy as np
import matplotlib.pyplot as plt

path = pathlib.Path(__file__).parent.joinpath("old_faithful.txt")
xs = np.loadtxt(path)

plt.scatter(xs[:, 0], xs[:, 1])
plt.xlabel("Eruption time (min)")
plt.ylabel("Waiting time (min)")
plt.show()

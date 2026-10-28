import matplotlib.pyplot as plt
import numpy as np


def main() -> int:
    x = np.linspace(0, 7, 100)
    z = np.random.normal(0, 1, 1000)
    print("sin(x)/cos(x) range: [-1.00, 1.00]")
    print(f"Histogram sample count: {z.size}")
    _, axes = plt.subplots(nrows=1, ncols=2, figsize=(13, 4))
    axes[0].plot(x, np.sin(x), label='sin(x)')
    axes[0].plot(x, np.cos(x), label='cos(x)')
    axes[0].set_title("Line plot")
    axes[0].get_legend()
    axes[0].set_ylabel("y")
    axes[0].set_xlabel("x")
    axes[0].grid()
    axes[1].hist(z, bins=50)
    axes[1].set_title("Histagram")
    axes[1].set_ylabel("count")
    axes[1].set_xlabel("value")
    axes[1].grid()
    plt.show()
    return 0
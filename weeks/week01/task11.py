import matplotlib.pyplot as plt
import numpy as np


def main() -> int: 
    x = np.linspace(0, 10, 50)
    y = 2.1 * x + np.random.uniform(-5, 5, 50)

    print("Generated 50 points for y = 2.1*x + 1.0 + noise")
    print(f"x range: [{x.min():.2f}, {x.max():.2f}]")
    print(f"y range: [{y.min():.2f}, {y.max():.2f}]")

    plt.scatter(x, y, c='green')
    plt.plot(x, 2.1 * x, c="orange")
    plt.title("Synthetic linear data with noise")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.show()
    return 0
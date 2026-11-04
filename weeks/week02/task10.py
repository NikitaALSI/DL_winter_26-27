import matplotlib.pyplot as plt
import numpy as np
import torch

from dl_lib.activations.functional import sigmoid


def main() -> int:
    x = np.linspace(-10, 10, 100)
    y = sigmoid(x)
    print(f"{'sigmoid(-10)':<12} = {y[0]:.6f}",
          f"{'sigmoid(0)':<12} = {y[49]:.6f}",
          f"{'sigmoid(10)':<12} = {y[99]:.6f}",
          f"Output range:[{y.min():.6f}, {y.max():.6f}]",
          f"{'PyTorch sigmoid(-10)':<12} = {torch.sigmoid(torch.tensor([-10]))}",
          sep="\n"
          )
    plt.plot(y)
    plt.title("sigmoid(x)")
    plt.xlabel("x")
    plt.ylabel("sigmoid(x)")
    plt.grid()
    plt.show()
    return 0
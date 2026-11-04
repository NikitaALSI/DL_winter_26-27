import numpy as np

from dl_lib.activations.functional import softmax, softmax_nan


def main() -> int:
    x = np.array([1.0, 2.0, 3.0])
    print("scores:", x)
    print("softmax:", softmax(x))
    print("sum of probabilities:", softmax(x).sum())
    print()
    x = np.array([1000.0, 1001.0, 1002.0])
    print("Large scores:", x)
    print("Naive softmax (unstable):", softmax_nan(x))
    print("Stable softmax:", softmax(x))
    return 0
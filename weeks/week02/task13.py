import numpy as np

from dl_lib.losses.functional import binary_cross_entropy, categorical_cross_entropy


def main() -> int:
    y_true = np.array([1.0, 0.0, 1.0])
    p = np.array([0.9, 0.2, 0.6])
    print(f"Binary cross-entropy on y_true={y_true}, p={p}: {binary_cross_entropy(y_true, p):.4f}")
    print(f"y_true={1}, p={0.999}(confidently right): loss={binary_cross_entropy(np.array([1]), np.array([0.999])):.4f}")
    print(f"y_true={1}, p={0.001}(confidently right): loss={binary_cross_entropy(np.array([1]), np.array([0.001])):.4f}")
    print()
    y_true = np.array([0, 1, 2])
    p = np.array([
            [0.7, 0.2, 0.1],
            [0.1, 0.8, 0.1],
            [0.2, 0.2, 0.6],
        ])
    print(f"Multiclass cross-entropy on y_true={y_true}: {categorical_cross_entropy(y_true, p):.4f}")
    print(f"y_true={1}, p={0.999}(confidently right): loss={categorical_cross_entropy(np.array([0]), np.array([0.999])):.4f}")
    print(f"y_true={1}, p={0.001}(confidently right): loss={categorical_cross_entropy(np.array([0]), np.array([0.001])):.4f}")
    return 0
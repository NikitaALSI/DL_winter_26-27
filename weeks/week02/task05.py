import numpy as np

from dl_lib.metrics import functional as f


def main() -> int:
    arr = np.array([0.1, 0.8, 0.4, 0.7, 0.9])
    print(f"Probabilities: {arr}")

    for t in range(1, 10, 2):
        print(f"threshhold={t/10}: predictions={f.apply_threshold(arr, t/10)}")
    return 0
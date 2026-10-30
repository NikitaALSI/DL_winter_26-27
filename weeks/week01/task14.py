import numpy as np

from dl_lib.preprocessing import functional


def main() -> int:
    arr = np.sort(np.random.randint(1, 9, 8).astype(float))
    print(f"Original: {arr}")
    min_max = functional.min_max_normalize(arr)
    standart = functional.standardize(arr)
    print(f"Min-max: {min_max}\nStandertize: {standart}\n")
    print(f"Min-max range: [{min_max.min():.4f}, {min_max.max():.4f}]")
    print(f"Standardized mean/std: {standart.mean():.4f} / {standart.std():.4f}")

    return 0
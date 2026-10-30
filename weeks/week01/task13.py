import numpy as np
from matplotlib import pyplot as plt


def main() -> int:
    Uniform = np.random.uniform(size=10000)
    Normal = np.random.normal(size=10000)
    Exponential = np.random.exponential(size=10000)

    print(f"""Uniform: mean=({Uniform.mean():.4f}), std=({Uniform.std():.5f}), min=({Uniform.min():.4f}), max=({Uniform.max():.4f})
Norma;: mean=({Normal.mean():.4f}), std=({Normal.std():.5f}), min=({Normal.min():.4f}), max=({Normal.max():.4f})
Exponential: mean=({Exponential.mean():.4f}), std=({Exponential.std():.5f}), min=({Exponential.min():.4f}), max=({Exponential.max():.4f})
""")

    _, axes = plt.subplots(1, 3, figsize=(13, 4))
    for i, arr in enumerate([Uniform, Normal, Exponential]):
        axes[i].hist(arr, bins=25)
        axes[i].set_title(list(locals().keys())[i])
        axes[i].set_xlabel("value")
        axes[i].set_ylabel("counr")
        axes[i].grid()
    plt.show()
    return 0
import time

import numpy as np


def main() -> int:
    mat = np.random.uniform(-5, 6, 10000000)
    start_loop = time.perf_counter()
    sum_loop = 0
    for x in mat:
        sum_loop += x
    finish_loop = time.perf_counter() - start_loop
    
    start_vec = time.perf_counter()
    sum_vec = np.sum(mat)
    finish_vec = time.perf_counter() - start_vec
    print(f"""Array length: {mat.size}
Loop sum: {sum_loop:.4f} ({finish_loop:.4f}s)
Vectorized sum: {sum_vec:.4f} ({finish_vec:.4f}s)
Vectorized speedup: {int(finish_loop/finish_vec)}x

Vectorized mean: {mat.mean():.4f}
Vectorized std: {mat.std():.4f}
Vectorized min/max: {mat.min():.4f} / {mat.max():.4f}
""")
    return 0
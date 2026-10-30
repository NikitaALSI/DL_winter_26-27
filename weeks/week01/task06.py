import numpy as np


def main() -> int:
    arr_1d = np.arange(1, 5)
    print(f"1D array (vector): shape={arr_1d.shape}, dtype={arr_1d.dtype}, ndim={arr_1d.ndim}, size={arr_1d.size}")
    print(arr_1d)
    arr_2d = np.arange(1, 7).reshape(2, 3)
    print(f"2D array (vector): shape={arr_2d.shape}, dtype={arr_2d.dtype}, ndim={arr_2d.ndim}, size={arr_2d.size}")
    print(arr_2d)
    arr_3d = np.arange(1, 25).reshape(2, 3, 4)
    print(f"3D array (vector): shape={arr_3d.shape}, dtype={arr_3d.dtype}, ndim={arr_3d.ndim}, size={arr_3d.size}")
    print(arr_3d)
    return 0

import numpy as np

from dl_lib.losses import functional


def main() -> int:
    y_true = np.array([3, 5, 7, 9], dtype=np.float32)
    y_pred = np.array([2, 6, 8, 7], dtype=np.float32)
    errors = functional.mse(y_true, y_pred)
    print(f"{"y_true:":<20}{y_true}",
          f"{"y_pred:":<20}{y_pred}",
          f"{"MSE:":<20}{errors:.4f}",
          sep="\n")

    y_pred_with_outlier = np.array([2, 6, 8, 100], dtype=np.float32)
    print(f"{"y_pred with one extreme outlier:":<20}{y_pred_with_outlier}",
          f"{"MAE with outliers:":<20}{functional.mae(y_true, y_pred_with_outlier)}",
          f"{"MSE with outliers:":<20}{functional.mse(y_true, y_pred_with_outlier)}",
          sep="\n")
    return 0
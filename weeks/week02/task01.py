import numpy as np


def main() -> int:
    y_true = np.array([3, 5, 7, 9])
    y_pred = np.array([2, 6, 8, 7])
    errors = y_pred - y_true

    print(f"{"y_true:":<20}{y_true}",
          f"{"y_pred:":<20}{y_pred}",
          f"{"errors:":<20}{errors}",
          "",
          f"mean error: {errors.mean():.4f}",
          f"MAE (mean absolute error): {np.abs(errors).mean():.4f}",
          f"MSE (mean squared error):  {(errors**2).mean():.4f}",
          f"RMSE (root mean squared error): {np.sqrt((errors**2).mean()):.4f}",
          sep="\n")
    return 0
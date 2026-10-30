import matplotlib.pyplot as plt
import numpy as np

from dl_lib.losses import functional as f


def main() -> int:
    y_true = np.array([3, 5, 7, 0], dtype=np.float32)
    y_pred = np.array([2, 6, 8, 0], dtype=np.float32)

    mae = []
    mse = []
    rmse = []
    for x in range(10):
        y_pred[-1] = x
        mae += [f.mae(y_true, y_pred)]
        mse += [f.mse(y_true, y_pred)]
        rmse += [f.rmse(y_true, y_pred)]
        if x % 3 == 0:
            print(f"Growing error={x:.1f}: MAE={mae[-1]:.4f}, MSE={mse[-1]:.4f}, RMSE={x:.4f}")

    plt.plot(np.arange(10), np.array(mae), label="MAE")
    plt.plot(np.arange(10), np.array(mse), label="MSE")
    plt.plot(np.arange(10), np.array(rmse), label="RMSE")
    plt.title("MAE, MSE and RMSE as one predicton error grows")
    plt.ylabel("loss value")
    plt.xlabel("the growing error, with other errors held fixed")
    plt.legend()
    plt.grid()
    plt.show()

    return 0
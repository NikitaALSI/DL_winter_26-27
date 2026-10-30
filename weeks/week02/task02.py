import numpy as np
import torch
from torch.nn.functional import l1_loss

from dl_lib.losses import functional


def main() -> int:
    y_true = np.array([3, 5, 7, 9], dtype=np.float32)
    y_pred = np.array([2, 6, 8, 7], dtype=np.float32)
    errors = functional.mae(y_true, y_pred)
    print(f"{"y_true:":<15}{y_true}",
          f"{"y_pred:":<15}{y_pred}",
          f"{"MAE:":<15}{errors:.4f}",
          sep="\n")

    print(f"{"MAE (torch):":<15}{l1_loss(torch.from_numpy(y_pred), torch.from_numpy(y_true))}")
    return 0
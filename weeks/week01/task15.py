import numpy as np
import torch


def main() -> int:
    arr = np.arange(1, 7, dtype=np.float32).reshape(2, 3)
    print(f"NumPy array:\n{arr}\ndtype={arr.dtype}, shape={arr.shape}")
    tensor = torch.from_numpy(arr)
    print(f"PyTorch tensor:\n{tensor}\ndtype={tensor.dtype}, shape={tensor.shape}, device={tensor.device}")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Selected device: {device}")
    tensor.to(device)
    print(f"Tensor moved to device: {device}, dtype={tensor.dtype}")

    return 0
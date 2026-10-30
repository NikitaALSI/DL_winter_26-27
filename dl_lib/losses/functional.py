import numpy as np


def mae(true: np.ndarray, pred: np.ndarray) -> float:
    error = pred - true
    return np.abs(error).mean()

def mse(true: np.ndarray, pred: np.ndarray) -> float:
    error = pred - true
    return (error**2).mean()

def rmse(true: np.ndarray, pred: np.ndarray) -> float:
    error = pred - true
    return np.sqrt((error**2).mean())

import numpy as np


def apply_threshold(array: np.ndarray, threshold: float) -> np.ndarray:
    return (array >= threshold).astype(int)

def confusion_matrix(true: np.ndarray, pred: np.ndarray) -> dict:
    ones = np.ones(shape=true.shape)
    return {
        "tp": int(ones[(true == 1) & (pred == 1)].sum()), 
        "tn": int(ones[(true == 0) & (pred == 0)].sum()), 
        "fp": int(ones[(true == 0) & (pred == 1)].sum()), 
        "fn": int(ones[(true == 1) & (pred == 0)].sum())
    }

def accuracy(true: np.ndarray, pred: np.ndarray):
    return (true[true == 1].size + pred[pred == 1].size) / true.size

def precision(true: np.ndarray, pred: np.ndarray):
    return true[true == 1].size/(true[true == 1].size + true[true == 0].size)
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

def binary_cross_entropy(labels: np.ndarray, probabilities: np.ndarray) -> float:
    return (-1/probabilities.size) * (labels * np.log(probabilities) + (1 - labels) * np.log(1 - probabilities)).sum()

def categorical_cross_entropy(labels: np.ndarray, probabilities: np.ndarray) -> float:
    try:
        return  (-1/probabilities.shape[0]) * sum(np.log(probabilities[x, x]) for x in labels)
    except IndexError:
        return  (-1/probabilities.shape[0]) * sum(np.log(probabilities[x]) for x in labels)

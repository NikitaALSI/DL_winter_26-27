import numpy as np


def sigmoid(array: np.ndarray):
    return 1 / (1 + np.e**-array)

def relu(array: np.ndarray):
    return np.where(array > 0, array, 0)

def tanh(array: np.ndarray):
    return np.tanh(array)

def softmax(array: np.ndarray):
    if len(array.shape) > 1:
        return np.array([np.exp(x - x.max()) / np.exp(x - x.max()).sum() for x in array])
    return np.exp(array - array.max()) / np.exp(array - array.max()).sum()

def softmax_nan(array: np.ndarray):
    if len(array.shape) > 1:
        return np.array([np.exp(x) / np.exp(x).sum() for x in array])
    return np.exp(array) / np.exp(array).sum()
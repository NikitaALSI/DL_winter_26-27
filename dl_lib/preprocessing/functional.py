import numpy as np


def min_max_normalize(arr: np.ndarray) -> np.ndarray:
    return ((arr - arr.min())/(arr.max() - arr.min())) * (1-0) + 0 if arr.std() != 0 else np.zeros(shape=arr.shape)

def standardize(arr: np.ndarray) -> np.ndarray:
    return (arr - arr.mean()) / arr.std() if arr.std() != 0 else np.zeros(shape=arr.shape)
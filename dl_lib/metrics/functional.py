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
    cf = confusion_matrix(true, pred)
    try:
        return (cf["tp"] + cf["tn"]) / (pred.size)
    except ZeroDivisionError:
        return 0

def precision(true: np.ndarray, pred: np.ndarray):
    cf = confusion_matrix(true, pred)
    try:
        return cf["tp"] / (cf["tp"] + cf["fp"])
    except ZeroDivisionError:
        return 0

def recall(true: np.ndarray, pred: np.ndarray):
    cf = confusion_matrix(true, pred)
    try:
        return cf["tp"] / (cf["tp"] + cf["fn"])
    except ZeroDivisionError:
        return 0

def f1_score(true: np.ndarray, pred: np.ndarray):
    cf = confusion_matrix(true, pred)
    try:
        return (2 * cf["tp"]) / (2 * cf["tp"] + cf["fp"] + cf["fn"])
    except ZeroDivisionError:
        return 0
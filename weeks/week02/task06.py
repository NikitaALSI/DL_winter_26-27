import numpy as np

from dl_lib.metrics import functional as f


def main() -> int:
    y_true = np.array([1, 0, 1, 0, 1])
    y_pred = np.array([1, 0, 0, 1, 1])
    confusion_matrix = f.confusion_matrix(y_true, y_pred)
    print(f"{"True positives:":<18}{confusion_matrix['tp']}",
          f"{"True negatives:":<18}{confusion_matrix['tn']}",
          f"{"False positives:":<18}{confusion_matrix['fp']}",
          f"{"False negatives:":<18}{confusion_matrix['fn']}",
          sep="\n")
    return 0

import numpy as np

from dl_lib.metrics.functional import accuracy, f1_score, precision, recall


def main() -> int:
    y_true = np.array([0] * 990 + [1] * 10)
    np.random.shuffle(y_true)
    y_pred = np.random.randint(0, 1, 1000)
    ac = accuracy(y_true, y_pred)
    pr = precision(y_true, y_pred)
    rc = recall(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    print("Dataset: 990 negative, 10 positive\nModel: always predicts negative, never looks at the input",
        f"{'  accuracy:':<15}{ac:.4f}",
        f"{'  precision:':<15}{pr:.4f}",
        f"{'  recall:':<15}{rc:.4f}",
        f"{'  precision:':<15}{f1:.4f}",
        sep="\n")
    return 0
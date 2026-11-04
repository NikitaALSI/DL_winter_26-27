import matplotlib.pyplot as plt
import numpy as np

from dl_lib.metrics.functional import apply_threshold, precision, recall


def main() -> int:
    y_probabilities = np.r_[np.random.normal(0.65, 1, 50), np.random.normal(0.05, 0.5, 50)]
    y_true = np.random.choice([0, 1], size=100, p=[0.5, 0.5])
    
    pr = []
    rc = []
    for x in range(30):
        t = x / 30
        y_pred = apply_threshold(y_probabilities, t)
        pr += [precision(y_true, y_pred)]
        rc += [recall(y_true, y_pred)]

        if x % 3 == 0 :
            print(f"threshold={t}: precision={pr[-1]:.4f}, recall={rc[-1]:.4f}")

    plt.plot(pr, "-o", label="precision")
    plt.plot(rc, "-o", label="recall")
    plt.xlabel("value")
    plt.ylabel("threshold")
    plt.legend()
    plt.grid()
    plt.show()
    
    return 0
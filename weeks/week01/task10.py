import numpy as np


def main() -> int:
    a = np.arange(1, 5).reshape(2, 2)
    print("A:", a, "", sep="\n")
    b = np.arange(5, 9).reshape(2, 2)
    print("B:", b, "", sep="\n")
    elwise = a * b
    print("Elementwise:", elwise, "", sep="\n")
    mat = a @ b
    print("Matrix multiplication:", mat, "", sep="\n")
    transp = a.transpose()
    print("The transpose of A:", transp, "", sep="\n")
    return 0
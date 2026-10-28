
import numpy as np


def main() -> int:
    mat = np.arange(1, 7).reshape(2, 3)
    print(f"""Matrix + scalar (10)
{mat + 10}

Matrix (2, 3) + row vector (3,):
{mat + np.arange(10, 40, 10)}

Matrix (2, 3) + column vector (2, 1)
{mat + np.arange(100, 300, 100).reshape(2, 1)}

Matrix (2, 3) + incompatible (2,) raises:""")
    try:
        err = mat + np.arange(100, 300, 100).reshape(2,)
        print(err)
    except ValueError as e:
        print(e)
    return 0
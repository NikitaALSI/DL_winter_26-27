import numpy as np


def main() -> int:
    matrix = np.random.randint(1, 12, size=12).reshape(3, 4)
    print(f"""Matrix:
{matrix}

Second row: {matrix[1, :]}
Third column: {matrix[:, 3]}
Submatrix: 
{matrix[-2:, -2:]}

Boolean mask for more than 7:
{matrix > 7}
Values satisfying the mask: {matrix[matrix > 7]}
    """)
    return 0
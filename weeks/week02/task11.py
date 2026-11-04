import matplotlib.pyplot as plt
import numpy as np

from dl_lib.activations.functional import relu, sigmoid, tanh


def main() -> int:
    x = np.linspace(-10, 10, 101)
    s = sigmoid(x)
    r = relu(x)
    t = tanh(x)
    print(f"""sigmoid range: [{s.min():.4f}, {s.max():.4f}]
relu range:    [{r.min():.4f}, {r.max():.4f}]
tanh range:    [{t.min():.4f}, {t.max():.4f}]

At x=-5: sigmoid={s[25]:.4f}, relu={r[25]:.4f}, tanh={t[25]:.4f}
At x=0:  sigmoid={s[50]:.4f}, relu={r[50]:.4f}, tanh={t[50]:.4f}
At x=5:  sigmoid={s[75]:.4f}, relu={r[75]:.4f}, tanh={t[75]:.4f}
""")

    plt.plot(s, label="sigmoid")
    plt.plot(r, label="relu")
    plt.plot(t, label="tanh")
    plt.title("sigmoid, relu, tanh")
    plt.xlabel("x")
    plt.ylabel("activation(x)")
    plt.grid()
    plt.show()
    return 0
import numpy as np
import matplotlib.pyplot as plt

def chebyshev_T(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return 2 * x * chebyshev_T(n - 1, x) - chebyshev_T(n - 2, x)

# Valores para graficar
x_vals = np.linspace(-1, 1, 400)
n_vals = [1, 2, 3, 4, 5]

plt.figure(figsize=(8, 6))
for n in n_vals:
    y_vals = [chebyshev_T(n, x) for x in x_vals]
    plt.plot(x_vals, y_vals, label=f"T_{n}(x)")

plt.title("Polinomios de Chebyshev de primer tipo T_n(x)")
plt.xlabel("x")
plt.ylabel("T_n(x)")
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def P_chebyshev(n, x):
    """Polinomio de Chebyshev de primer tipo usando la recurrencia P_{n+1}(x) = x P_n(x) - P_{n-1}(x)"""
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * P_chebyshev(n - 1, x) - P_chebyshev(n - 2, x)

def formula_trig(n, theta):
    """\frac{sin((n+1)\theta)}{sin(\theta)}"""
    return np.sin((n + 1) * theta) / np.sin(theta)

# Rango de theta evitando 0 para evitar división por cero
theta = np.linspace(0.01, np.pi - 0.01, 400)
n = 5
x = 2 * np.cos(theta)

# Polinomio de Chebyshev evaluado en x
P_vals = [P_chebyshev(n, xi) for xi in x]
# Fórmula trigonométrica
trig_vals = formula_trig(n, theta)

plt.figure(figsize=(8, 6))
plt.plot(theta, P_vals, label=f"P_{n}(2cos(θ)) por recurrencia")
plt.plot(theta, trig_vals, '--', label=r"$sin((n+1)\theta)/sin(\theta)$")
plt.xlabel(r"$\theta$")
plt.ylabel(r"Valor")
plt.title(f"Comparación: P_{{n}}(2cos(θ)) vs sin((n+1)θ)/sin(θ) para n={n}")
plt.legend()
plt.grid(True)
plt.show()

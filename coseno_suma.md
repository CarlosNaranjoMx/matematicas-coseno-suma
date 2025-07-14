# Índice
1. [Identidad del coseno de la suma](#identidad-del-coseno-de-la-suma)
2. [Demostración geométrica](#demostración-geométrica-usando-el-círculo-unitario)
3. [Deducción de la matriz de rotación](#deducción-de-la-matriz-de-rotación)
4. [Conclusión](#conclusión)

# Identidad del coseno de la suma

La identidad trigonométrica para el coseno de la suma de dos ángulos es:

$$
\cos(a + b) = \cos a \cos b - \sin a \sin b
$$

# Demostración geométrica usando el círculo unitario

Consideremos dos ángulos $a$ y $b$ en el círculo unitario. Los puntos correspondientes son:
- $P_a = (\cos a, \sin a)$
- $P_b = (\cos b, \sin b)$

La rotación por $a$ seguida de una rotación por $b$ equivale a una rotación por $a + b$.

# Deducción de la matriz de rotación

La matriz de rotación por un ángulo $\theta$ en el plano se deduce así:

Si rotamos el punto $(x, y)$ por un ángulo $\theta$ respecto al origen, las nuevas coordenadas $(x', y')$ son:

$$
\begin{align*}
x' &= x \cos \theta - y \sin \theta \\
y' &= x \sin \theta + y \cos \theta
\end{align*}
$$

Esto se puede escribir en forma matricial:

$$
\begin{pmatrix}
x' \\
y'
\end{pmatrix} =
\begin{pmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
$$

Por lo tanto, la matriz de rotación es:
$$
R(\theta) = \begin{pmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{pmatrix}
$$

Multiplicando las matrices de rotación:
$$
R(a) R(b) = R(a + b)
$$

Calculando el producto:
$$
\begin{pmatrix}
\cos a & -\sin a \\
\sin a & \cos a
\end{pmatrix}
\begin{pmatrix}
\cos b & -\sin b \\
\sin b & \cos b
\end{pmatrix}
$$

El elemento (1,1) del resultado es:
$$
\cos a \cos b - \sin a \sin b
$$

Por lo tanto:
$$
\cos(a + b) = \cos a \cos b - \sin a \sin b
$$

# Conclusión

La fórmula se demuestra usando la composición de rotaciones en el plano, y se verifica algebraicamente con matrices de rotación.

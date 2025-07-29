import numpy as np
import matplotlib.pyplot as plt

# Crear valores para x en el dominio de arccos [-1, 1]
x = np.linspace(-1, 1, 1000)
y = np.arccos(x)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='arccos(x)')

# Configurar la gráfica
plt.title('Función Arcocoseno (arccos)', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('arccos(x)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)

# Agregar líneas de referencia importantes
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axhline(y=np.pi/2, color='r', linestyle='--', alpha=0.7, label='π/2')
plt.axhline(y=np.pi, color='r', linestyle='--', alpha=0.7, label='π')
plt.axvline(x=0, color='k', linewidth=0.5)

# Marcar puntos importantes
points_x = [-1, -0.5, 0, 0.5, 1]
points_y = [np.arccos(x) for x in points_x]
plt.scatter(points_x, points_y, color='red', s=50, zorder=5)

# Agregar etiquetas a los puntos importantes
labels = [f'({x:.1f}, {y:.2f})' for x, y in zip(points_x, points_y)]
for i, (x_val, y_val, label) in enumerate(zip(points_x, points_y, labels)):
    plt.annotate(label, (x_val, y_val), xytext=(5, 5), textcoords='offset points', fontsize=10)

# Configurar límites y ticks
plt.xlim(-1.1, 1.1)
plt.ylim(-0.2, np.pi + 0.2)
plt.xticks([-1, -0.5, 0, 0.5, 1])
plt.yticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi], 
          ['0', 'π/4', 'π/2', '3π/4', 'π'])

plt.tight_layout()

# Guardar la gráfica
plt.savefig('grafica_arccos.png', dpi=300, bbox_inches='tight')
plt.savefig('grafica_arccos.pdf', bbox_inches='tight')

# Mostrar la gráfica
plt.show()

print("Gráfica del arccos guardada como 'grafica_arccos.png' y 'grafica_arccos.pdf'")

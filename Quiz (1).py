import random
import matplotlib.pyplot as plt
import numpy as np

# Número de puntos aleatorios a generar
num_puntos = 100000

# Inicializar listas para almacenar coordenadas
x_inside = []
y_inside = []
x_outside = []
y_outside = []

# Generar puntos aleatorios y determinar si están dentro del círculo
for _ in range(num_puntos):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

# Estimar el valor de pi
pi_estimate = 4 * len(x_inside) / num_puntos

# Crear gráfico
plt.figure(figsize=(8, 8))
plt.scatter(x_inside, y_inside, color='blue', marker='.')
plt.scatter(x_outside, y_outside, color='red', marker='.')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Estimación de Pi utilizando Montecarlo')
plt.axis('equal')

# Guardar el gráfico en un archivo PDF
plt.savefig('montecarlo_pi.pdf')

# Mostrar la estimación de pi
print(f'Estimación de pi: {pi_estimate:.7f}')

# Mostrar el gráfico en la pantalla
plt.show()

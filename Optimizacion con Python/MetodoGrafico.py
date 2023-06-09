import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Funcion objetiva: Max Z = 9000x + 1200y
# Restricciones: x <= 20, y <= 10, 3x + 4y >= 12

x = np.linspace(0, 25, 100)

# Definir restricciones
y1 = 10 + (0 * x)
x1 = 20 + (0 * y1)
y2 = (12 - (3 * x)) / 4
x_limites = (0, None)
y_limites = (0, None)

# Definir funcion objetivo
y3 = (-9000 * x) / 1200

# Graficar restricciones
plt.plot(x1, x, label = 'x <= 20')
plt.plot(x, y1, label = 'y <= 10')
plt.plot(x, y2, label = '3x + 4y >= 12')

# Graficar funcion objetivo
plt.plot(x, y3, label = 'Z = 9000x + 1200y')

plt.fill_between(x, 0, x1, where = (x1 >= 0) & (x >= 0), alpha = 0.1)
plt.fill_between(x, 0, y1, where = (y1 >= 0) & (x >= 0), alpha = 0.1)
plt.fill_between(x, 0, y2, where = (y2 >= 0) & (x >= 0), alpha = 0.1)

plt.xlim(x_limites)
plt.ylim(y_limites)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Método Gráfico')
plt.legend()

# Encontrar el vertice factible
A = np.array([[1, 0], [0, 1], [3, 4]])
b = np.array([20, 10, 12])
c = np.array([-9000, -1200])
resultado = linprog(c, A_ub = A, b_ub = b)

def funcion_objetivo(x, y):
    return 9000*x + 1200*y

if resultado.success:
    if funcion_objetivo == -resultado.fun:
        # Agregar el punto de la solucion factible
        vertice_factible = (resultado.x[0], resultado.x[1])
        plt.plot(vertice_factible[0], vertice_factible[1], 'ro', label = "Punto factible")
        print("Solucion factible: Z = ", -resultado.fun)
        print("x = ", resultado.x[0])
        print("y = ", resultado.x[1])
    else:
        print("Tiene infinitas soluciones")
else:
    print("No tiene solucion factible")
    
plt.show()
from scipy.optimize import linprog

# Funcion objetiva: Max z = 110x, 150y
# Restricciones: 4x + 6y <= 480, 20x + 10y <= 1500 

# Definir restricciones
A = [[4, 6], [20, 10]]
b = [480, 1500]

# Definir funcion objetivo
c = [-110, -150] # Coeficientes de la funcion objetivo para maximizar
resultado = linprog(c, A_ub = A, b_ub = b)

if resultado.success:
    # El valor de Z es el opuesto del valor devuelto por linprog
    print("Solucion factible: Z = ", -resultado.fun)
    print("x = ", resultado.x[0])
    print("y = ", resultado.x[1])
else:
    print("No tiene solucion factible")
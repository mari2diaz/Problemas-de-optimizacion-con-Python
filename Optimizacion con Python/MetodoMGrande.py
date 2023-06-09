import pulp

# Funcion objetiva: Min Z = 6x + 2y
# Restricciones: 0.5x + 0.2y <= 4, 2x + 3y >= 20, x + y = 10

# Crear el problema de programacion lineal
problema = pulp.LpProblem("Problema de Programacion Lineal", pulp.LpMinimize)

# Definir variables de decision
x = pulp.LpVariable("x", lowBound = 0)
y = pulp.LpVariable("y", lowBound = 0)

# Definir funcion objetivo
problema += 6*x + 2*y, "Funcion Objetivo"

# Definir restricciones
problema += 0.5*x + 0.2*y >= 4, "Restriccion 1"
problema += 2*x + 3*y >= 20, "Restriccion 2"
problema += x + y == 10, "Restriccion 3"

# Resolver el problema utilizando el metodo M Grande
problema.solve()

# Verificar si se encontro una solucion factible
if problema.status == 1:
    print("Solucion factible: Z = ", pulp.value(problema.objective))
    print("x = ", pulp.value(x))
    print("y = ", pulp.value(y))
else:
    print("No se encontro una solucion factible")
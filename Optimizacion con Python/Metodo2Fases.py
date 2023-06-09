import pulp

# Funcion objetivo: Min Z = 6x + 2y
# Restricciones: x + 2y >= 4, 3x + 2y >= 8

# Crear el problema de programacion lineal
problema = pulp.LpProblem("Problema de Programacion Lineal", pulp.LpMinimize)

# Definir variables de decision
x = pulp.LpVariable("x", lowBound = 0)
y = pulp.LpVariable("y", lowBound = 0)

# Definir funcion objetivo
problema += 6*x + 2*y, "Funcion Objetivo"

# Definir restricciones
problema += x + 2*y >= 4, "Restriccion 1"
problema += 3*x + 2*y >= 8, "Restriccion 2"

# Resolver el problema utilizando el metodo de las dos fases
problema.solve()

# Verificar si se encontro una solucion factible inicial
if problema.status == 1:
    print("Se encontro una solucion factible inicial")

    # Resolver nuevamente el problema sin las variables artificiales
    problema2 = pulp.LpProblem("Problema de Programacion Lineal", pulp.LpMinimize)

    # Definir variables de decision
    x = pulp.LpVariable("x", lowBound = 0)
    y = pulp.LpVariable("y", lowBound = 0)

    # Definir funcion objetivo
    problema2 += 6*x + 2*y, "Funcion Objetivo"

    # Definir restricciones sin las variables artificiales
    problema2 += x + 2*y >= 4, "Restriccion 1"
    problema2 += 3*x + 2*y >= 8, "Restriccion 2"

    # Resolver el problema sin las variables artificiales
    problema2.solve()

    # Imprimir solucion factible
    print("Solucion factible: Z = ", pulp.value(problema2.objective))
    print("x = ", pulp.value(x))
    print("y = ", pulp.value(y))
else:
    print("No se encontro una solucion factible")
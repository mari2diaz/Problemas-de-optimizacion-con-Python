import pulp

# Crear el problema de programación lineal
problema = pulp.LpProblem("Problema de Transporte", pulp.LpMinimize)

# Definir los silos y molinos
silos = ["silo1", "silo2", "silo3", "silo4"]
molinos = ["molino1", "molino2", "molino3", "molino4"]

# Definir los costos de transporte
costos = {
    "silo1": {"molino1": 10, "molino2": 2, "molino3": 20, "molino4": 11},
    "silo2": {"molino1": 7, "molino2": 9, "molino3": 24, "molino4": 12},
    "silo3": {"molino1": 4, "molino2": 14, "molino3": 16, "molino4": 18},
    "silo4": {"molino1": 5, "molino2": 15, "molino3": 15, "molino4": 15},
}

# Crear las variables de decisión
envios = pulp.LpVariable.dicts("Envios", (silos, molinos), lowBound=0, cat="Integer")

# Definir la función objetivo
problema += pulp.lpSum([envios[silo][molino] * costos[silo][molino] for silo in silos for molino in molinos]), "Costo total de transporte"

# Definir las restricciones de oferta
oferta = {
    "silo1": 15,
    "silo2": 25,
    "silo3": 10,
    "silo4": 15
}
for silo in silos:
    problema += pulp.lpSum([envios[silo][molino] for molino in molinos]) <= oferta[silo], f"Oferta del silo {silo}"

# Definir las restricciones de demanda
demanda = {
    "molino1": 11,
    "molino2": 15,
    "molino3": 20,
    "molino4": 15
}
for molino in molinos:
    problema += pulp.lpSum([envios[silo][molino] for silo in silos]) >= demanda[molino], f"Demanda del molino {molino}"

# Resolver el problema
problema.solve()

# Imprimir la solución
print("Estado del problema:", pulp.LpStatus[problema.status])
print("Costo total de transporte:", pulp.value(problema.objective))
for silo in silos:
    for molino in molinos:
        cantidad = pulp.value(envios[silo][molino])
        if cantidad > 0:
            print(f"Enviar {cantidad} camiones cargados del silo {silo} al molino {molino}")
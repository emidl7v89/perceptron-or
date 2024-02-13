import random

# Tabla de verdad OR
tabla_verdad = [
    ([0, 0, 0, 1], 0),
    ([0, 0, 1, 1], 1),
    ([0, 1, 0, 1], 1),
    ([0, 1, 1, 1], 1),
    ([1, 0, 0, 1], 1),
    ([1, 0, 1, 1], 1),
    ([1, 1, 0, 1], 1),
    ([1, 1, 1, 1], 1)
]

# Inicializar los pesos
w = [random.random() for _ in range(4)]

# Función de activación
def activacion(y):
    return 1 if y > 0 else 0 if y < 0 else 0

# Entrenamiento del perceptrón
for _ in range(100):  # Número de épocas
    for x, salida_esperada in tabla_verdad:
        y = sum(xi * wi for xi, wi in zip(x, w))  # Función sumatoria
        error = salida_esperada - activacion(y)  # Cálculo del error
        if error != 0:  # Si hay error, actualizar los pesos
            w = [wi + error * xi for xi, wi in zip(x, w)]

# Imprimir los pesos finales
print("Pesos finales:")
for i, wi in enumerate(w):
    print(f"w{i}: {wi}")

# Evaluar las entradas con los pesos finales
for x, salida_esperada in tabla_verdad:
    y = sum(xi * wi for xi, wi in zip(x, w))  # Función sumatoria
    print(f"Entradas: {x[:-1]} Salida esperada: {salida_esperada} Suma ponderada: {y} Salida: {activacion(y)}")

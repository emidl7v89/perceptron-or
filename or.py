import random

# Definir la nueva tabla de verdad OR
truth_table = [
    ([0, 0, 0, 1], 0),
    ([0, 0, 1, 1], 1),
    ([0, 1, 0, 1], 1),
    ([0, 1, 1, 1], 1),
    ([1, 0, 0, 1], 1),
    ([1, 0, 1, 1], 1),
    ([1, 1, 0, 1], 1),
    ([1, 1, 1, 1], 1)
]

# Función de activación
def activation_function(y):
    return 1 if y >= 0 else 0

# Función para entrenar el perceptrón OR
def train_perceptron():
    # Inicializar pesos aleatorios dentro del rango [-10, 10]
    w = [random.randint(-10, 10) for _ in range(4)]  # w0, w1, w2, w3

    error = True
    while error:
        error = False
        for x_sample, y_desired in truth_table:
            # Agregar bias a la entrada
            x = x_sample

            # Calcular la sumatoria
            y = sum([w[i] * x[i] for i in range(4)])

            # Aplicar función de activación
            y = activation_function(y)

            # Calcular error
            error_calc = y_desired - y

            # Actualizar pesos si hay error
            if error_calc != 0:
                error = True
                for i in range(4):
                    w[i] += error_calc * x[i]

    return w

# Probar el entrenamiento del perceptrón OR
weights = train_perceptron()
print("Pesos finales:")
print(f"w0: {weights[0]}")
print(f"w1: {weights[1]}")
print(f"w2: {weights[2]}")
print(f"w3: {weights[3]}")

# Mostrar resultados para cada entrada
for x_sample, y_desired in truth_table:
    # Calcular la sumatoria
    weighted_sum = sum([weights[i] * x_sample[i] for i in range(4)])

    # Aplicar función de activación
    y = activation_function(weighted_sum)

    print(f"Entradas: {x_sample[:3]} Salida esperada: {y_desired} Suma ponderada: {weighted_sum} Salida: {y}")

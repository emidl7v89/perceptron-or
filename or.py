import random
import csv


class PerceptronO:
    def __init__(self):
        self.factores = [random.randint(-5, 5) for _ in range(3)]  # Factores aleatorios entre -5 y 5 para las tres entradas
        self.bias = random.randint(-5, 5)  # Bias aleatorio entre -5 y 5

    def calcular(self, inputs):
        suma_ponderada = sum(input * factor for input, factor in zip(inputs, self.factores)) + self.bias
        output = 1 if suma_ponderada > 0 else 0
        return suma_ponderada, output


def testear_combinaciones(perceptron):
    inputs = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1]
    ]
    output_esperado = [0, 1, 1, 1, 1, 1, 1, 1]  # Salidas esperadas para la compuerta OR

    iteracion = 0
    while True:
        iteracion += 1
        print(f'\nIteración #{iteracion}')
        print(f'w1={perceptron.factores[0]}\nw2={perceptron.factores[1]}\nw3={perceptron.factores[2]}\nSesgo={perceptron.bias}')

        todas_correctas = True  # Flag para verificar si todas las salidas son correctas

        for input, output_esp in zip(inputs, output_esperado):
            suma_ponderada, output = perceptron.calcular(input)
            print(
                f'Entradas: {input}, Salida esperada: {output_esp}, Suma ponderada: {suma_ponderada}, Salida: {output}')

            # Actualizar factores si la salida no coincide con la salida esperada
            if output != output_esp:
                todas_correctas = False
                for i in range(3):
                    perceptron.factores[i] = random.randint(-5, 5)
                perceptron.bias = random.randint(-5, 5)

        if todas_correctas:
            print("\nSolución:")
            print(f'w1={perceptron.factores[0]}\nw2={perceptron.factores[1]}\nw3={perceptron.factores[2]}\nSesgo={perceptron.bias}')
            guardar_solucion(perceptron)
            return


def guardar_solucion(perceptron):
    with open("solucion_o.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([perceptron.factores[0], perceptron.factores[1], perceptron.factores[2], perceptron.bias])


def cargar_factores_desde_archivo():
    try:
        with open("solucion_o.csv", "r") as f:
            reader = csv.reader(f)
            factores = next(reader)
            perceptron_o = PerceptronO()
            perceptron_o.factores = [float(factor) for factor in factores]
            return perceptron_o
    except FileNotFoundError:
        return None


def evaluar_manualmente(perceptron):
    while True:
        opcion = input("¿Desea evaluar una entrada x1,x2,x3? (Si/No): ").capitalize()
        if opcion == 'Si':
            x1 = int(input("Ingrese x1: "))
            x2 = int(input("Ingrese x2: "))
            x3 = int(input("Ingrese x3: "))
            suma_ponderada, salida = perceptron.calcular([x1, x2, x3])
            print(f'Suma ponderada: {suma_ponderada}, Salida: {salida}')
        elif opcion == 'No':
            break
        else:
            print("Opción inválida. Por favor, seleccione 'Si' para sí o 'No' para no.")


perceptron_o = cargar_factores_desde_archivo()

if perceptron_o is None:
    perceptron_o = PerceptronO()

testear_combinaciones(perceptron_o)
guardar_solucion(perceptron_o)
evaluar_manualmente(perceptron_o)

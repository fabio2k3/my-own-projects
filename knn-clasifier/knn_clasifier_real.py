import math


# DATASET
dataset = [
    {"peso": 150, "color": "Rojo",     "fruta": "Manzana"},
    {"peso": 155, "color": "Rojo",     "fruta": "Manzana"},
    {"peso": 160, "color": "Rojo",     "fruta": "Manzana"},

    {"peso": 175, "color": "Naranja",  "fruta": "Naranja"},
    {"peso": 180, "color": "Naranja",  "fruta": "Naranja"},
    {"peso": 185, "color": "Naranja",  "fruta": "Naranja"},

    {"peso": 115, "color": "Amarillo", "fruta": "Banano"},
    {"peso": 120, "color": "Amarillo", "fruta": "Banano"},
    {"peso": 125, "color": "Amarillo", "fruta": "Banano"},
]

# CODIFICACIÓN DE COLORES

# Convertimos los colores a números para poder calcular
# distancias matemáticas.

colores = {
    "Rojo": 0,
    "Naranja": 1,
    "Amarillo": 2
}


# ENTRADA DEL USUARIO

peso = float(input("Introduce el peso de la fruta (g): "))
color = input("Introduce el color de la fruta: ").strip().capitalize()

# Validar que el color exista

if color not in colores:
    print("Color no válido.")
    exit()

color_num = colores[color]

# VALOR DE K
K = 3



# CALCULAR DISTANCIAS

# Aquí almacenaremos:

# [distancia, nombre_fruta]
distancias = []

for fruta in dataset:

    # Peso de la fruta del dataset
    peso_dataset = fruta["peso"]

    # Color convertido a número
    color_dataset = colores[fruta["color"]]

    # Distancia Euclídea
    distancia = math.sqrt(
        (peso - peso_dataset) ** 2 +
        (color_num - color_dataset) ** 2
    )

    # Guardamos la distancia junto con la fruta
    distancias.append([distancia, fruta["fruta"]])


# ORDENAR POR DISTANCIA
distancias.sort(key=lambda x: x[0])


# TOMAR LOS K VECINOS MÁS CERCANOS
vecinos = distancias[:K]


# VOTACIÓN
votos = {}

for vecino in vecinos:

    fruta = vecino[1]

    if fruta in votos:
        votos[fruta] += 1
    else:
        votos[fruta] = 1


# BUSCAR LA FRUTA MÁS VOTADA

mejor_fruta = None
mayor_votos = 0

for fruta, cantidad in votos.items():

    if cantidad > mayor_votos:
        mayor_votos = cantidad
        mejor_fruta = fruta


# RESULTADO
print("\n===== RESULTADO =====")
print(f"Peso: {peso}")
print(f"Color: {color}")
print(f"K = {K}")
print(f"La fruta predicha es: {mejor_fruta}")


# MOSTRAR LOS VECINOS
print("\nVecinos más cercanos:")

for distancia, fruta in vecinos:
    print(f"{fruta:10} Distancia = {distancia:.2f}")
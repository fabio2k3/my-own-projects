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

# Entrada de Datos (Usuario)
peso = float(input("Introduce el peso de la fruta (g): "))
color = input("Introduce el color de la fruta: ").strip().capitalize()

# Lista donde guardaremos los posibles candidatos
candidates = []

for f in dataset:
    if f["color"] == color:
        candidates.append([f["peso"], f["fruta"]])

pos = 0

# NO hay candiadtos => Buscamos la que tenga un peso más cercano
if len(candidates) == 0:
    mindif = abs(peso - dataset[0]["peso"])

    for i in range(1, len(dataset)):
        if abs(dataset[i]["peso"] - peso) < mindif:
            mindif = abs(dataset[i]["peso"] - peso)
            pos = i

    print(f"La fruta con peso: {peso} y color: {color}, es: {dataset[pos]['fruta']}")

# SI hay candidatos => Buscamos la que tenga un peso más cercano del mismo color
else:
    if len(candidates) == 1:
        print(candidates[0][1])

    else:
        mindif = abs(peso - candidates[0][0])

        for i in range(1, len(candidates)):
            if abs(candidates[i][0] - peso) < mindif:
                mindif = abs(candidates[i][0] - peso)
                pos = i

        print(f"La fruta con peso: {peso} y color: {color}, es: {candidates[pos][1]}")
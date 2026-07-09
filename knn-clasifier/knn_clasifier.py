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

peso = float(input("Introduce el peso de la fruta (g): "))
color = input("Introduce el color de la fruta: ").strip().capitalize()

candidates = []

for f in dataset:
    if f[color] == "Rojo":
        candidates.append([f["peso"], f["fruta"]])

pos = 0
if len(candidates) == 1:
    print(candidates[0][1])
else:
    mindif = abs(peso - candidates[0][1])
    for i in range(1, len(candidates)):
        if abs(candidates[i][0]-peso) < mindif:
            mindif = abs(candidates[i][0]-peso)
            pos = i

print(f"La fruta es {candidates[pos][0]}")
        
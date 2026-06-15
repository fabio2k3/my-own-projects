import random

X = []
Y = []

for i in range(20):
    x = random.randint(1, 10)
    X.append(x)

    y = random.randint(1,10)
    Y.append(y)

print("Datos X:")
print(X)
print("Datos Y:")
print(Y)

n = len(X)

mediaX = 0
mediaY = 0

for i in range(n):
    mediaX += X[i]
    mediaY += Y[i]

mediaX /= n
mediaY /= n

# Pendiente de la Recta
beta1 = 0.0
numerador_beta1 = 0.0
denominador_beta1 = 0.0

for i in range(n):
    numerador_beta1 += (X[i] - mediaX)*(Y[i] - mediaY)
    denominador_beta1 += (X[i] - mediaX)**2

beta1 = numerador_beta1 / denominador_beta1

# Punto donde la recta corta al eje Y
beta0 = mediaY - beta1*mediaX

def prediccionFuncion(x, beta1, beta0):
    return x*beta1 + beta0

print(f"Función resultante: y = {beta1}*x + {beta0}")
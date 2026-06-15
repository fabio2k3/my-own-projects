import random
import matplotlib.pyplot as plt
import numpy as np
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

x_line = np.linspace(min(X), max(X), 100)
y_line = beta1 * x_line + beta0

plt.plot(X, Y, 'o')
plt.xlabel("Valores X")
plt.ylabel("Valores Y")
plt.title("Mis Datos")
plt.grid(True)

plt.plot(x_line, y_line, 'r-', linewidth = 2, label = f"Recta y = {beta1}*x + {beta0}"  )

plt.show()
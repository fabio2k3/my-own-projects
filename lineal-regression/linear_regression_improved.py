import random
import matplotlib.pyplot as plt
import numpy as np
import math

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

print("\n")
print(f"Función resultante: y = {beta1}*x + {beta0}")
print("\n")

# R^2 (Coeficiente de Determinación)
SS_res = 0
for i in range(n):
    SS_res += (Y[i] - (beta1 * X[i] + beta0)) ** 2

SS_tot = 0
for i in range(n): 
    SS_tot += (Y[i] - mediaY)**2

R2 = 1 - (SS_res / SS_tot) 
print("El Coeficiente de Determinación es:")
print(f"R^2 = {R2}")
print("\n")


# MSE (Error Cuadrático Medio)
MSE = SS_res / n
print("El Error Cuadrátoco Medio es: ")
print(f"MSE = {MSE}")
print("\n")


# Correlación entre X e Y (r de Pearson)
numerador_r = numerador_beta1
denominador_r = 0
dem_r_X = 0
dem_r_Y = 0
for i in range(n):
    dem_r_X += (X[i] - mediaX)**2
    dem_r_Y += (Y[i] - mediaY)**2
denominador_r = math.sqrt(dem_r_X * dem_r_Y)
r_Pearson = numerador_r / denominador_r
print(f"Correlacion entre X e Y (r de Pearson): r = {r_Pearson}")
if abs(r_Pearson) < 0.3:
    print("Correlación débil: no hay relación lineal significativa")
elif r_Pearson > 0:
    print("Correlación positiva: a mayor X, mayor Y")
else:
    print("Correlación negativa: a mayor X, menor Y")
print("\n")

# Calcular predicciones para líneas de error
Y_pred = [beta1 * x + beta0 for x in X]

# Mostrar métricas de forma más detallada (opcional, ya las tienes pero podemos mejorar)
print("\n=== MÉTRICAS DEL MODELO ===")
print(f"R² = {R2:.4f}  ({R2*100:.2f}% de varianza explicada)")
print(f"MSE = {MSE:.4f}")
print(f"RMSE = {MSE**0.5:.4f}")
print(f"Correlación (r) = {r_Pearson:.4f}")
print(f"Relación r² = {r_Pearson**2:.4f} (debe ser igual a R²)")
print("\n")

# ===== VISUALIZACIÓN MEJORADA =====
plt.figure(figsize=(10, 6))

# Datos originales
plt.scatter(X, Y, color='blue', s=80, alpha=0.7, 
           label='Datos Observados', zorder=3)

# Recta de regresión (extendida)
x_line = np.linspace(min(X)-1, max(X)+1, 100)
y_line = beta1 * x_line + beta0
plt.plot(x_line, y_line, 'r-', linewidth=2.5, 
        label=f'Recta: y = {beta1:.3f}x + {beta0:.3f}', zorder=2)

# Líneas de error (residuos)
for i in range(n):
    plt.plot([X[i], X[i]], [Y[i], Y_pred[i]], 
            'gray', linestyle='--', linewidth=0.8, alpha=0.5)

# Agregar texto con métricas en el gráfico
texto_metricas = f'R² = {R2:.4f}\nMSE = {MSE:.4f}\nr = {r_Pearson:.4f}'
plt.text(0.05, 0.95, texto_metricas, transform=plt.gca().transAxes,
        fontsize=11, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Mostrar beta0 y beta1 en el gráfico
texto_coeficientes = f'β₀ = {beta0:.3f}\nβ₁ = {beta1:.3f}'
plt.text(0.05, 0.75, texto_coeficientes, transform=plt.gca().transAxes,
        fontsize=11, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Personalizar gráfico
plt.xlabel("Valores X", fontsize=12)
plt.ylabel("Valores Y", fontsize=12)
plt.title("Regresión Lineal - Análisis de Datos", fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(loc='best', fontsize=10)
plt.tight_layout()

plt.show()
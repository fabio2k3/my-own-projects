# Primera Idea (Implementación Básica de una LR)
# Nombre del Código: linear_ regression.py  (python lineal-regression/linear_regression.py)


En esta primera implementación te toman datos randos y se guardan en los array X y Y:

Cada par de posiciones xi (perteneciente a X) y yi (perteneciente a Y), forman los pares (xi, yi) que se toman como base para obtener los puntos clave de nuestra regresión.

Nuestra función tiene la forma clásica de una LR: f(x) = beta1 * x + beta0

Beta 1: dice si hay tendencia positiva o negativa en nuestros datos (básicamente es la pendiente)

Beta 2: punto donde la recta corta al eje de las Y cuando xi = 0

# VERSIÓN linear_regression_improved (python lineal-regression/linear_regression_improved.py)

En esta versión agregamos los siguientes conceptos para añadirle maoyr profundidad y profesionalidad a nuestro codigo.

R^2: Mide qué proporción de variabilidad total de Y es explicada por nuestro modelo de regresión lineal. Este valor siempre está 0 y 1

MSE (Error Cuadrático Medio): Es el promedio de los errores al cuadrado. Nos dice, en promedio, qué tan lejos están nuestras predicciones de los valores reales. Es la métrica más común para evaluar a precisión de un modelo de regresión.

Correlación de Pearson(r) entre X e Y: Mide la fuerza y la dirección lineal entre dos variables X e Y. Su valor está siempre entre -1 y 1.

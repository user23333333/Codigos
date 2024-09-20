import math

def litres(time):
    # Calcula los litros de agua y redondea hacia abajo
    return math.floor(time * 0.5)

# Ejemplos de uso
print(litres(3))    # 1
print(litres(6.7))  # 3
print(litres(11.8)) # 5

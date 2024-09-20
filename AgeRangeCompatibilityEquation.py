import math


def dating_range(age):
    if age <= 14:
        # Cálculo del rango usando la regla especial para edades menores o iguales a 14
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    else:
        # Cálculo del rango usando la regla clásica "mitad de tu edad más siete"
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)

    return f"{min_age}-{max_age}"


# Ejemplos de uso
print(dating_range(27))  # "20-40"
print(dating_range(5))  # "4-5"
print(dating_range(17))  # "15-20"

def animal_years(humanYears):
    # Inicializamos las edades en años de gato y perro
    catYears = 0
    dogYears = 0

    # Lógica para el cálculo de años de gato y perro
    if humanYears >= 1:
        catYears = 15
        dogYears = 15
    if humanYears >= 2:
        catYears += 9
        dogYears += 9
    if humanYears > 2:
        catYears += (humanYears - 2) * 4
        dogYears += (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]

# Ejemplo de uso:

print(animal_years(10)) # [10, 56, 64]

def total_pressure(M1, M2, m1, m2, V, T):
    # Constante del gas en unidades apropiadas
    R = 0.082

    # Convertir la temperatura a Kelvin
    T_kelvin = T + 273.15

    # Calcular la cantidad de moles de cada gas
    n1 = m1 / M1
    n2 = m2 / M2

    # Calcular la cantidad total de moles
    n_total = n1 + n2

    # Calcular la presión total
    P_total = (n_total * R * T_kelvin) / V

    return P_total


# Ejemplos de uso
print(total_pressure(44, 28, 10, 20, 10, 25))  # ejemplo con datos de entrada
print(total_pressure(50, 20, 5, 10, 2, 100))  # otro ejemplo

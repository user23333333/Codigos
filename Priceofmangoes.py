def mango(quantity, price):
    # Calcula cuántos mangos se pagan y cuántos son gratis
    paid_mangoes = (quantity // 3) * 2 + (quantity % 3)
    # Calcula el costo total
    total_cost = paid_mangoes * price
    return total_cost

# Ejemplos de uso
print(mango(2, 3))  # 6
print(mango(3, 3))  # 6
print(mango(5, 3))  # 12
print(mango(9, 5))  # 30

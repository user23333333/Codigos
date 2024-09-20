def usd_to_cny(usd):
    # Realiza la conversión de USD a CNY
    cny = usd * 6.75
    # Devuelve el resultado formateado como una cadena con dos decimales
    return f"{cny:.2f} Chinese Yuan"

# Ejemplos de uso
print(usd_to_cny(15))   # '101.25 Chinese Yuan'
print(usd_to_cny(465))  # '3138.75 Chinese Yuan'
print(usd_to_cny(100))  # '675.00 Chinese Yua
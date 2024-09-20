def nba_extrap(ppg, mpg):
    # Manejar el caso en el que mpg es 0
    if mpg == 0:
        return 0
    # Calcular los puntos extrapolados a 48 minutos y redondear a un decimal
    ppg_48 = (ppg * 48) / mpg
    return round(ppg_48, 1)

# Ejemplos de uso
print(nba_extrap(12, 20))  # 28.8
print(nba_extrap(10, 10))  # 48
print(nba_extrap(5, 17))   # 14.1
print(nba_extrap(0, 0))    # 0

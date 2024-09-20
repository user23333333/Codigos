import math

def convert_to_16_9_resolution(x, y):
    # Calcula el nuevo ancho basado en la relación de aspecto 16:9
    new_x = math.ceil((16 / 9) * y)
    # Devuelve la nueva resolución manteniendo la misma altura
    return new_x, y

# Ejemplos de uso
print(convert_to_16_9_resolution(1920, 1080))  # (1920, 1080)
print(convert_to_16_9_resolution(1440, 1080))  # (1920, 1080)
print(convert_to_16_9_resolution(1024, 768))   # (1366, 768)
print(convert_to_16_9_resolution(800, 600))    # (1067, 600)

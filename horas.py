# Ejemplo de horas

#Es necesario importar las depencendias necesarias
from datetime import datetime, date, time, timedelta
import calendar

ahora = datetime.now()  # Obtiene fecha y hora actual
print("Fecha y Hora:", ahora)  # Muestra fecha y hora
print("Fecha y Hora UTC:",ahora.utcnow())  # Muestra fecha/hora UTC

print("Horas:")
hora1 = time(10, 5, 0)  # Asigna 10h 5m 0s
print("\tHora1:", hora1)
hora2 = time(23, 15, 0)  # Asigna 23h 15m 0s
print("\tHora2:", hora2)

# Compara horas
print("\tHora1 < Hora2:", hora1 < hora2)  # True

import pandas as pd

def BS(ds):
    # Obtener el día del mes
    date = pd.to_datetime(ds, format='%Y-%m-%d')
    day_of_month = date.day
    month = date.month
    year = date.year
    day_of_week = date.weekday()
    
    if ((day_of_month == 15 or day_of_month == 30) and day_of_week in range(5)):
        return 1
    elif (((month == 2 and day_of_month in [28, 29]) or day_of_month in [26]) and day_of_week in range(5)):
        return 1
    elif day_of_week == 4 and day_of_month in [13, 14, 28, 29]:
        return 1
    return 0


# Ejemplo de uso
print("15 de febrero",BS("2024-02-15"))    
print("28 de febrero",BS("2023-02-28"))
print("29 de febrero",BS("2024-02-29"))
print("29 de marzo",BS("2024-03-29"))
print("29 de ferero",BS("2024-02-29"))  # Salida: 1 (primer quincena de febrero)
print("15 de marzo",BS("2024-03-15"))  # Salida: 1 (segunda quincena de febrero)
print("30 de marzo",BS("2024-03-30"))  # Salida: 0 (fuera de quincenas)
print("15 de junio",BS("2024-06-15"))  # Salida: 1 (primer quincena de junio)
print("30 de junio",BS("2024-06-30"))  # Salida: 1 (segunda quincena de junio)
print("28 de junio",BS("2024-06-28"))
print("11 de julio",BS("2024-07-11"))
print("28 de febrero",BS("2021-02-28"))
print("27 de febrero",BS("2021-02-27"))
print("26 de febrero",BS("2021-02-26"))
print("26 de febrero",BS("2022-02-26"))
print("26 de febrero 2023",BS("2023-02-26"))
print("15 de febrero 2023",BS("2023-02-15"))
print("27 de febrero 2023",BS("2023-02-27"))
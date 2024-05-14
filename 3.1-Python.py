datos_climaticos = {
    "Ciudad de México": [29, 28, 30, 26, 29, 25, 31],
    "Nueva York": [17, 22, 16, 28, 15, 38, 20],
    "Toronto": [14, 15, 12, 10, 11, 15, 17],
}

for ciudad in datos_climaticos:
    print(
        f"""
Ciudad: {ciudad}
Temperatura promedio: {round(sum(datos_climaticos[ciudad])/len(datos_climaticos[ciudad]), 2)}
Temperatura máxima: {max(datos_climaticos[ciudad])}
Temperatura mínima: {min(datos_climaticos[ciudad])}
"""
    )

import pandas as pd
from datetime import datetime
import numpy as np

file = "Prueba_Promociones.csv"

df = pd.read_csv(file)


def input_ususario():
    fecha_inicio = input("Ingresa la fecha de inicio (yyyymmmdd): ")
    if fecha_inicio != "":
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y%m%d")

    fecha_fin = input("Ingresa la fecha de fin (yyyymmdd): ")
    if fecha_fin != "":
        fecha_fin = datetime.strptime(fecha_fin, "%Y%m%d")

    categoria = input("Ingresa la categoria: ")

    uso = input("Ingresa el uso: ")

    while True:
        sku = input("Ingresa el SKU: ")
        try:
            sku = int(sku)
        except ValueError:
            break

    porcentaje = float(input("Ingresa el porcentaje: "))

    inventario_inicial = float(input("Ingresa el inventario inicial: "))

    return fecha_inicio, fecha_fin, categoria, uso, sku, porcentaje, inventario_inicial


df["Fecha"] = pd.to_datetime(df["Fecha"], format="%d-%m-%y %H:%M")

df["Semana"] = df["Fecha"].dt.isocalendar().week


def filtro(df, f_inicio, f_fin, porcentaje, uso, categoria):

    if f_inicio != "" and f_fin == "":
        df = df[df["Fecha"] >= pd.to_datetime(f_inicio)]
    elif f_inicio == "" and f_fin != "":
        df = df[df["Fecha"] <= pd.to_datetime(f_fin)]
    elif f_inicio != "" and f_fin != "":
        df = df[
            (df["Fecha"] <= pd.to_datetime(f_fin))
            & (df["Fecha"] >= pd.to_datetime(f_inicio))
        ]

    df = df[df["Modelo"] != "real"]

    if uso != "" and categoria == "":
        df = df[df["Uso"] == uso]
    elif uso == "" and categoria == "":
        pass
    elif uso == "" and categoria != "":
        df = df[df["Categoria"] == categoria]

    df["Piezas"] = df["Piezas"] + (df["Piezas"] * (porcentaje / 100))

    return df


fecha_inicio, fecha_fin, categoria, uso, sku, porcentaje, inventario_inicial = (
    input_ususario()
)

df_temp = filtro(df, fecha_inicio, fecha_fin, porcentaje, uso, categoria)
print(df_temp)

import requests
import csv
import json
from datetime import datetime

carpeta_csvs = "C://Users//Nicolas.Cortes.L//Desktop//Python//WeatherData//carpeta_csvs"
carpeta_jsons = "C://Users//Nicolas.Cortes.L//Desktop//Python//WeatherData//carpeta_jsons"
lat = -23.561390
lon = -70.391882

def kelvin_celsius_transformacion(obj, tipo_temperatura, tiempo_temperatura):
    return round((obj.get(tipo_temperatura,"").get(tiempo_temperatura,"") - 273.15), 2)

def unix_fecha(obj, tiempo_dia):
    return datetime.fromtimestamp(obj.get(tiempo_dia,""))

def kelvin_celsius_hora(obj, tiempo_hora):
    return round((obj.get(tiempo_hora,"") - 273.15), 2)

def obtener_datos():
    excluir = "daily,minutely,alerts"
    encabezados = ["Fecha y Hora",
                   "Temperatura (°C)",
                   "Percepción",
                   "Presión (hPa)",
                   "Humedad (%)",
                   "dew_point",
                   "Radiación",
                   "Nubes",
                   "Visibilidad (KM)",
                   "Velocidad Del Viento",
                   "wind_deg",
                   "wind_gust"]
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={excluir}&appid={APIkey}"
    r = requests.get(url, timeout = 20)
    data = r.json()
    resultados_datos1 = data["hourly"]

    with open(f"{carpeta_jsons}//clima_hora.json","w") as file:
        json.dump(data, file, indent = 5)

    with open(f"{carpeta_csvs}//datos_hora.csv", "w", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames = encabezados)
        writer.writeheader()

    with open(f"{carpeta_csvs}//datos_hora.csv", "a", newline = "") as file:
       writer = csv.DictWriter(file, fieldnames= encabezados)
       for obj in resultados_datos1:
           writer.writerow({
               "Fecha y Hora" : unix_fecha(obj, tiempo_dia = "dt"),
               "Temperatura (°C)" : kelvin_celsius_hora(obj, tiempo_hora = "temp"),
               "Percepción" : kelvin_celsius_hora(obj, tiempo_hora = "feels_like"),
               "Presión (hPa)" : obj.get("pressure",""),
               "Humedad (%)" : obj.get("humidity",""),
               "dew_point" : obj.get("dew_point",""),
               "Radiación" : obj.get("uvi",""),
               "Nubes" : obj.get("clouds",""),
               "Visibilidad (KM)" : obj.get("visibility",""),
               "Velocidad Del Viento" : obj.get("wind_speed",""),
               "wind_deg" : obj.get("wind_deg",""),
               "wind_gust" : obj.get("wind_gust","")
           })

def obtener_datos2():
    excluir = "hourly,alerts,minutely,current"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={excluir}&appid={APIkey}"
    r = requests.get(url)
    data = r.json()
    encabezados = ["Fecha y Hora",
                    "Amanecer",
                    "Atardecer",
                    "Salidad de la Luna",
                    "Puesta de la Luna",
                    "Fase Lunar",
                    "Summary",
                    "Temperatura dia (°C)",
                    "Temperatura min (°C)",
                    "Temperatura max (°C)",
                    "Temperatura noche (°C)",
                    "Temperatura atardecer (°C)",
                    "Temperatura amanecer (°C)",
                    "Percepción dia (°C)",
                    "Percepción noche (°C)",
                    "Percepción atardecer (°C)",
                    "Percepción amanecer (°C)",
                    "Presión (hPa)",
                    "Humedad (%)",
                    "Temperatura atmosférica",
                    "Velocidad del Viento (m/s)",
                    "Dirección del viento (°)",
                    "Ráfaga de viento",
                    "Clima ID",
                    "Clima Parametros",
                    "Clima descripción",
                    "Clima icono",
                    "Nubes (%)",
                    "Probabilidad de Lluvia",
                    "Radiación"]

    resultados_datos_diarios = data["daily"]

    with open(f"{carpeta_jsons}//clima_diario.json","w") as file:
        json.dump(data, file, indent = 5)

    with open(f"{carpeta_csvs}//datos_diario.csv", "w", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames = encabezados)
        writer.writeheader()

    with open(f"{carpeta_csvs}//datos_diario.csv", "a", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames = encabezados)
        for obj in resultados_datos_diarios:
            writer.writerow({
                "Fecha y Hora" : unix_fecha(obj,tiempo_dia = "dt"),
                "Amanecer" : unix_fecha(obj,tiempo_dia = "sunrise"),
                "Atardecer" : unix_fecha(obj,tiempo_dia = "sunset"),
                "Salidad de la Luna" : unix_fecha(obj,tiempo_dia = "moonrise"),
                "Puesta de la Luna" : unix_fecha(obj,tiempo_dia = "moonset"),
                "Fase Lunar" : obj.get("moon_phase",""),
                "Summary" : obj.get("summary",""),
                "Temperatura dia (°C)" : kelvin_celsius_transformacion(obj, tipo_temperatura = "temp", tiempo_temperatura = "day"),
                "Temperatura min (°C)" : kelvin_celsius_transformacion(obj, tipo_temperatura = "temp", tiempo_temperatura = "min"),
                "Temperatura max (°C)" : kelvin_celsius_transformacion(obj, tipo_temperatura = "temp", tiempo_temperatura = "max"),
                "Temperatura noche (°C)" : kelvin_celsius_transformacion(obj, tipo_temperatura = "temp", tiempo_temperatura = "night"),
                "Temperatura atardecer (°C)" : kelvin_celsius_transformacion(obj, tipo_temperatura = "temp", tiempo_temperatura = "eve"),
                "Temperatura amanecer (°C)" : kelvin_celsius_transformacion(obj, tipo_temperatura = "temp", tiempo_temperatura = "morn"),
                "Percepción dia (°C)" : kelvin_celsius_transformacion(obj, tipo_temperatura = "feels_like", tiempo_temperatura = "day"),
                "Percepción noche (°C)" : kelvin_celsius_transformacion(obj, tipo_temperatura = "feels_like", tiempo_temperatura = "night"),
                "Percepción atardecer (°C)" : kelvin_celsius_transformacion(obj, tipo_temperatura = "feels_like", tiempo_temperatura = "eve"),
                "Percepción amanecer (°C)" : kelvin_celsius_transformacion(obj, tipo_temperatura = "feels_like", tiempo_temperatura = "morn"),
                "Presión (hPa)" : obj.get("pressure",""),
                "Humedad (%)" : obj.get("humidity",""),
                "Temperatura atmosférica" : obj.get("dew_point",""),
                "Velocidad del Viento (m/s)" : obj.get("wind_speed",""),
                "Dirección del viento (°)" : obj.get("wind_deg",""),
                "Ráfaga de viento" : obj.get("wind_gust",""),
                "Clima ID" : obj.get("weather","[]")[0].get("id",""),
                "Clima Parametros" : obj.get("weather","[]")[0].get("main",""),
                "Clima descripción" : obj.get("weather","[]")[0].get("description",""),
                "Clima icono" : obj.get("weather","[]")[0].get("icon",""),
                "Nubes (%)" : obj.get("clouds",""),
                "Probabilidad de Lluvia" : obj.get("pop",""),
                "Radiación" : obj.get("uvi","")
            })

def obtener_datos_minutos():
    excluir = "hourly,alerts,daily,current"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={excluir}&appid={APIkey}"
    r = requests.get(url)
    data = r.json()
    resultados_minutos = data["minutely"]
    encabezados = ["Fecha y Hora", "Precipitacion (%)"]

    with open(f"{carpeta_jsons}//clima_minutos.json", "w") as file:
        json.dump(resultados_minutos, file, indent = 5)

    with open(f"{carpeta_csvs}//datos_minutos.csv", "w", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames = encabezados)
        writer.writeheader()

    with open(f"{carpeta_csvs}//datos_minutos.csv", "a", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames = encabezados)
        for obj in resultados_minutos:
            writer.writerow({"Fecha y Hora" : unix_fecha(obj, tiempo_dia = "dt"),
                             "Precipitacion (%)" : obj.get("precipitation", "")})

obtener_datos()
obtener_datos2()
obtener_datos_minutos()

import json
import os
import csv

carpeta = "/content/drive/MyDrive/PythonRoles"
lista = [f for f in os.listdir(carpeta) if f.endswith('.json')]

def lista_de_PythonRoles():
    master_csv = os.path.join(carpeta, "master.csv")
    fieldnames = ["Nombre", "Email", "Contrato", "Rol"]

    with open(master_csv, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    for name in lista:
        for index, valor in enumerate(name):
            if valor == "_":
                Rol = name[:index]

        with open(f"/content/drive/MyDrive/PythonRoles/{name}", "r", encoding="utf-8-sig") as file:
            data = json.load(file)
            results = data["d"]["results"]

        with open(master_csv, "a", newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for obj in results:
                writer.writerow({
                    "Nombre": obj.get("Title", ""),
                    "Email": obj.get("Email", ""),
                    "Contrato": obtener_contrato(results),
                    "Rol": Rol
                })

def obtener_contrato(results):
    contrato = results[0]["Groups"]["__deferred"]["uri"][43:]
    for key,value in enumerate(contrato):
        if value == "/":<
            contrato = contrato[:key]
            break
    return contrato

lista_de_PythonRoles()

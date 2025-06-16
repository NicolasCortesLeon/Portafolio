## Script Python Finning

Este es un script que fue hecho en mi práctica profesional en Finning durante Enero y Febrero de 2025, específicamente en el Centro de formación técnica bajo el área de Gestión Operacional en Antofagasta. Toma todos los archivos en una carpeta de GoogleDrive terminados en .json, los procesa y guarda en archivos CSV para luego ser usados en un reporte en PowerBI.

Este código sirve como Back-up ya que también hallé una solución que se conecta a una carpeta de SharePoint desde PowerBI y se pueden manipular los archivos json en PowerQuery de PowerBI.

Aquí se muestra el proceso en el cual se realizan 33 solicitudes HTTP a SharePoint mediante Power Automate, cuyas respuestas están en formato JSON. Power Automate utiliza la API de Microsoft, lo que permitió evitar la creación de una aplicación en Azure Active Directory (Azure AD). Esto se debe a que, por políticas de la empresa, la creación de aplicaciones en Azure AD debe ser solicitada formalmente, y el proceso de aprobación y respuesta suele ser largo. Por ello, no fue necesaria la creación de dicha aplicación.

![Image](https://github.com/user-attachments/assets/e0a58743-bdd7-4482-891b-73c97a380ae5)

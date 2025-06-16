##  Práctica Finning

Este es el trabajo que fue hecho en mi práctica profesional en Finning durante Enero y Febrero de 2025, específicamente en el Centro de formación técnica bajo el área de Gestión Operacional y Reportabilidad en Antofagasta. En mi experiencia en la práctica pude idear 2 soluciones para el problema, una mediante Power Automate y PowerBI, y otra como Back-up usando Python.

Aquí se muestra el proceso en el cual se realizan 33 solicitudes HTTP a SharePoint mediante Power Automate, cuyas respuestas están en formato JSON. Power Automate utiliza la API de Microsoft, lo que permitió evitar la creación de una aplicación en Azure Active Directory (Azure AD). Esto se debe a que, por políticas de la empresa, la creación de aplicaciones en Azure AD debe ser solicitada formalmente, y el proceso de aprobación y respuesta suele ser largo. Por ello, no fue necesaria la creación de dicha aplicación.

![Image](https://github.com/user-attachments/assets/7317877e-5af7-41d0-b937-55d05b429fd6)

Luego, todos los archivos json son almacenados en una carpeta de SharePoint, esto mediante acciones de PowerAutomate.

![Image](https://github.com/user-attachments/assets/9a4b162f-911e-4cc5-9c1a-30135c2670c5)

Posteriormente, mediante Power BI, se extraen los archivos almacenados en la carpeta de SharePoint. Power BI, además de permitir conexiones a servicios como APIs o carpetas en la nube (tipo Drive), también puede acceder a carpetas de SharePoint y procesar archivos en formato json. Gracias a estas capacidades, fue posible elaborar el reporte directamente a partir de los archivos generados.

![Image](https://github.com/user-attachments/assets/f5464419-54e9-4c33-b8eb-ccafca40e7ab)

Por último, la solución de respaldo (Back-up) reutiliza el flujo de procesos de la primera alternativa. La diferencia principal es que los archivos JSON son almacenados en una carpeta, ya sea en Google Drive o en OneDrive (Microsoft). Posteriormente, estos archivos pueden ser descargados mediante un notebook de Google Colab o desde una máquina virtual, para luego ser procesados y generar el reporte correspondiente.

![Image](https://github.com/user-attachments/assets/87c55fd2-12e7-4570-b8f0-4b7145f8d833)

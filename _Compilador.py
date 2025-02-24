import PyInstaller.__main__
import os
import shutil

# Definir el nombre del ejecutable y la carpeta de salida
exe_name = "NetStatus_v1.0"
output_dir = "dist"

# Ejecutar PyInstaller con las opciones necesarias
PyInstaller.__main__.run([
    "--onefile",  # Genera un solo ejecutable
    "--windowed",  # Oculta la consola (para aplicaciones GUI)
    f"--name={exe_name}",  # Nombre del ejecutable
    "--icon=lib/resources/icons/icono.ico",  # Ruta al ícono
    f"--add-data=lib/resources{os.pathsep}lib/resources",  # Copiar la carpeta de recursos
    "_NetStat.py"  # Archivo principal
])

# ** Copiar manualmente la carpeta lib/resources a dist/ **
dest_folder = os.path.join(output_dir, "lib/resources")

if os.path.exists(dest_folder):
    shutil.rmtree(dest_folder)  # Elimina la carpeta si ya existe

shutil.copytree("lib/resources", dest_folder)  # Copia la carpeta completa
print("Ready...")

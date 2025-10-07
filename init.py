import os
import urllib.request
import zipfile

def init(force_download=False):
    """
    Descarga y prepara las carpetas 'gen-py' y 'local/data' desde tu repositorio de GitHub.
    """

    # URL base del ZIP de tu repositorio (ajusta tu usuario y repo)
    repo_zip_url = "https://github.com/danielfce01/Taller-1-Data-Streaming/archive/refs/heads/main.zip" 
    zip_path = "repo.zip"

    # Descargar solo si se pide o no existe
    if force_download or not os.path.exists(zip_path):
        print("⬇️ Descargando repositorio desde GitHub...")
        urllib.request.urlretrieve(repo_zip_url, zip_path)
    else:
        print("✅ Archivo ZIP ya descargado localmente.")

    # Extraer el contenido
    extract_path = "repo"
    if not os.path.exists(extract_path):
        print("📦 Extrayendo archivos...")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)
    else:
        print("✅ Archivos ya extraídos.")

    # Mover las carpetas necesarias a local/
    repo_name = os.listdir(extract_path)[0]  # nombre auto del repo
    src_path = os.path.join(extract_path, repo_name)

    os.makedirs("local", exist_ok=True)
    os.system(f"cp -r {src_path}/gen-py .")
    os.system(f"cp -r {src_path}/local/data local/")

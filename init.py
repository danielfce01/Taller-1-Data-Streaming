import os
import urllib.request
import zipfile

def init(force_download=False):
    """
    Descarga y prepara las carpetas 'gen-py' y 'local/data' desde el repositorio.
    """

    # URL del ZIP del repo (ajusta si tu repo tiene otro nombre)
    repo_zip_url = "https://github.com/danielfce01/Taller-1-Data-Streaming/archive/refs/heads/main.zip"
    zip_path = "repo.zip"

    if force_download or not os.path.exists(zip_path):
        print("⬇️ Descargando repositorio desde GitHub...")
        urllib.request.urlretrieve(repo_zip_url, zip_path)
    else:
        print("✅ Archivo ZIP ya descargado localmente.")

    extract_path = "repo"
    if not os.path.exists(extract_path):
        print("📦 Extrayendo archivos...")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)
    else:
        print("✅ Archivos ya extraídos.")

    repo_name = os.listdir(extract_path)[0]
    src_path = os.path.join(extract_path, repo_name)

    os.makedirs("local", exist_ok=True)
    os.system(f"cp -r {src_path}/gen-py .")
    os.system(f"cp -r {src_path}/local/data local/")

    print("✅ Carpetas 'gen-py' y 'local/data' listas para usar.")


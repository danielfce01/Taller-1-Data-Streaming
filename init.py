course_id = 'Taller-1-Data-Streaming'
github_repo = 'danielfce01/%s' % course_id
zip_file_url = "https://github.com/%s/archive/refs/heads/main.zip" % github_repo

def get_last_modif_date(localdir):
    try:
        import time, os, pytz
        import datetime
        k = datetime.datetime.fromtimestamp(max(os.path.getmtime(root) for root,_,_ in os.walk(localdir)))
        localtz = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
        k = k.astimezone(localtz)
        return k
    except Exception:
        return None

import requests, zipfile, io, os, shutil

def init(force_download=False):
    if force_download or not os.path.exists("local"):
        print("⬇️ Replicando recursos del repositorio...")
        dirname = course_id + "-main/"

        if os.path.exists(dirname):
            shutil.rmtree(dirname)

        r = requests.get(zip_file_url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()

        if os.path.exists("local"):
            shutil.rmtree("local")

        shutil.move(dirname + "/local", "local")

        if os.path.exists("gen-py"):
            shutil.rmtree("gen-py")
        shutil.move(dirname + "/gen-py", "gen-py")

        shutil.rmtree(dirname)
        print("✅ Carpetas 'local' y 'gen-py' listas para usar.")
    else:
        print("✅ Recursos locales ya disponibles.")

import os
from werkzeug.utils import secure_filename

EXTENSOES_PERMITIDAS = {"png", "jpg", "jpeg"}

def arquivo_permitido(nome_arquivo):
    return (
        "." in nome_arquivo and
        nome_arquivo.rsplit(".", 1)[1].lower() in EXTENSOES_PERMITIDAS
    )

def salvar_escudo(file, nome_time):
    if not file or file.filename == "":
        return None

    if not arquivo_permitido(file.filename):
        return None

    extensao = file.filename.rsplit(".", 1)[1].lower()
    nome_seguro = secure_filename(nome_time.lower().replace(" ", "_"))
    nome_final = f"{nome_seguro}.{extensao}"

    pasta = "static/uploads/escudos"
    os.makedirs(pasta, exist_ok=True)

    caminho = os.path.join(pasta, nome_final)
    file.save(caminho)

    return f"/{caminho}"

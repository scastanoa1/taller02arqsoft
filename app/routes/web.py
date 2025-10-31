import os
import platform
import random
from flask import Blueprint, render_template
from app.data.pokeneas import POKENEAS
from ..services.s3 import url_for_key


web_bp = Blueprint("web", __name__)

def get_container_id():
    return os.environ.get("HOSTNAME") or platform.node()

@web_bp.get("/")
@web_bp.get("/pokenea")
def show_random_pokenea():
    p = random.choice(POKENEAS)
    img_url = url_for_key(p["imagen_key"])
    return render_template(
        "pokenea.html",
        nombre=p["nombre"],
        frase=p["frase"],
        img_url=img_url,
        container_id=get_container_id()
    )

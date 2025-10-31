import os
import platform
import random
from flask import Blueprint, jsonify
from app.data.pokeneas import POKENEAS

api_bp = Blueprint("api", __name__)

def get_container_id():
    return os.environ.get("HOSTNAME") or platform.node()

@api_bp.get("/pokeneas/random")
def random_pokenea():
    p = random.choice(POKENEAS)
    return jsonify({
        "id": p["id"],
        "nombre": p["nombre"],
        "altura_m": p["altura_m"],
        "habilidad": p["habilidad"],
        "container_id": get_container_id()
    })

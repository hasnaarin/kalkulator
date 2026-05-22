from flask import Blueprint

bp = Blueprint("arithmetic", __name__, url_prefix="/arithmetic")

@bp.route("", methods=["GET", "POST"])
def index():
    return "Arithmetic Stub"

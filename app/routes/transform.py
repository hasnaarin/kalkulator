from flask import Blueprint

bp = Blueprint("transform", __name__, url_prefix="/transform")

@bp.route("", methods=["GET", "POST"])
def index():
    return "Transform Stub"

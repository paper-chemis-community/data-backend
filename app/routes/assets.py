from flask import Blueprint, send_file
from ..utils import assets

asset_bp = Blueprint("asset", __name__, "/asset")

@asset_bp.route("/pic/<id>")
def search_matter(id: str):
    path = "../resources/assets/pics/" + assets.readPicPath(id)
    return send_file(path)

@asset_bp.route("/sound/<id>")
def select_matter(id: str):
    path = "../resources/assets/sounds/" + assets.readSoundPath(id) 
    return send_file(path)
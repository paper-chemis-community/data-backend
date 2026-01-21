'''
资源文件读取路由
'''
from flask import Blueprint, send_file
from ..utils import assets

asset_bp = Blueprint("asset", __name__, "/asset")

@asset_bp.route("/list")
def asset_list():
    return assets.readAssetsList()

@asset_bp.route("/pic/<id>")
def find_pic(id: str):
    path = "../resources/assets/pics/" + assets.readPicPath(id)
    return send_file(path)

@asset_bp.route("/sound/<id>")
def find_sound(id: str):
    path = "../resources/assets/sounds/" + assets.readSoundPath(id) 
    return send_file(path)
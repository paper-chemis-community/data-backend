from flask import Blueprint, jsonify

page_bp = Blueprint("page", __name__, "/")

@page_bp.route("/")
def index():
    return jsonify({"code": "200", "message": "Service normal"})
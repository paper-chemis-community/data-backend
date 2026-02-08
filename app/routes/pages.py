'''
网页路由
'''
from flask import Blueprint, jsonify
from ..utils import index

page_bp = Blueprint("page", __name__, "/")

@page_bp.route("/")
def index_page():
    return jsonify({"code": "200", "message": "Service normal"})

@page_bp.route("/index")
def description():
    return jsonify(index.readIndex())
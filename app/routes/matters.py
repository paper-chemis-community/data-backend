'''
物质定义文件读取路由
'''
from flask import Blueprint
from ..utils import matters

matter_bp = Blueprint("matter", __name__, "/matter")

@matter_bp.route("/list")
def matter_list():
    return matters.readMatterList()

@matter_bp.route("/id/<id>")
def search_matter(id):
    return matters.readMatter(id)
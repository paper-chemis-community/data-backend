from flask import Blueprint
from ..utils import matters

matter_bp = Blueprint("matter", __name__, "/matter")

@matter_bp.route("/id/<id>")
def search_matter(id):
    return matters.readMatter(id)

@matter_bp.route("/match/<id>")
def select_matter(id):
    return id
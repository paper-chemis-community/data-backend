from flask import Blueprint
from ..services import matters

matter_bp = Blueprint("matter", __name__, "/matter")

@matter_bp.route("/<id>")
def search_matter(id):
    return matters.readMatter(id)
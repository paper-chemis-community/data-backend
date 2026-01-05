from flask import Blueprint
from ..services import reactions

reaction_bp = Blueprint("reaction", __name__, "/reaction")

@reaction_bp.route("/<id>")
def search_card(id):
    return reactions.readReaction(id)
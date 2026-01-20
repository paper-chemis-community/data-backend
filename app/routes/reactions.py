from flask import Blueprint
from ..utils import reactions

reaction_bp = Blueprint("reaction", __name__, "/reaction")

@reaction_bp.route("/id/<id>")
def search_reaction(id):
    return reactions.readReaction(id)
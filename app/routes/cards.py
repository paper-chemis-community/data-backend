from flask import Blueprint
from ..utils import cards

card_bp = Blueprint("card", __name__, "/card")

@card_bp.route("/id/<id>")
def search_card(id):
    return cards.readCard(id)
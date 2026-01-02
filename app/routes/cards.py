from flask import Blueprint
from ..services import cards

card_bp = Blueprint("card", __name__, "/card")

@card_bp.route("/<id>")
def search_card(id):
    return cards.readCard(id)
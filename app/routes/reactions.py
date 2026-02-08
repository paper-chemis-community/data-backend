'''
反应定义文件读取路由
'''
from flask import Blueprint, jsonify
from ..utils import reactions

reaction_bp = Blueprint("reaction", __name__, "/reaction")

@reaction_bp.route("list")
def reaction_list():
    return jsonify(reactions.readReactionList())

@reaction_bp.route("/match")
def match_list():
    return jsonify(reactions.readMatchList())

@reaction_bp.route("/id/<id>")
def search_reaction(id):
    return jsonify(reactions.readReaction(id))

@reaction_bp.route("/match/<id>")
def select_reaction(id):
    return jsonify(reactions.selectReaction(id))
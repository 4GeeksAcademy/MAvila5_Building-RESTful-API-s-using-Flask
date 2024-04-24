from flask import Flask, request, jsonify, url_for, Blueprint
from models import Pokemon, db
from utils import APIException

api = Blueprint('api', __name__)

@api.route('/test', methods=['GET'])
def testAPI():
    return jsonify('Your API Works, Congrats'), 200

@api.route('/test', methods=['POST'])
def postTest():
    return jsonify('THIS IS A POST RESPONSE'), 200

## Actual API EndPoint:
@api.route('/pokemon', methods=['POST'])
def add_pokemon():
    rb = request.get_json()
    pokemon = Pokemon(name=rb["name"], height=rb["height"], weight=rb["weight"], category=rb["category"])
    db.session.add(pokemon)
    db.session.commit()
    return f"Pokemon {rb['name']} was added to our database", 200
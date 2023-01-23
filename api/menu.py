from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
import json

menu_api = Blueprint('menu_api', __name__, url_prefix='/api/menu')
api = Api(menu_api)

class MenuAPI:
    class _Read(Resource):
        def get(self):
            with open('menu.json') as menu_file:
                items = json.load(menu_file)
            return jsonify(items)

    api.add_resource(_Read, '/')

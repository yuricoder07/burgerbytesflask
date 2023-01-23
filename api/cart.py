from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
import json
from flask import request

cart_api = Blueprint('cart_api', __name__, url_prefix='/api/cart')
api = Api(cart_api)

class Cart:
    def __init__(self):
        self.items = []
        self.cart_items = {}
        self.register_routes()

    def register_routes(self):
        class _Create(Resource):
            def post(self):
                body = request.get_json()
                item = body.get('item')
                price = body.get('price')
                description = body.get('description')
                self.items.append({'item': item, 'price': price, 'description': description})
                return jsonify({'message': 'Item added to menu'}), 201

        class _Read(Resource):
            def get(self):
                return jsonify(self.items)

        class _Cart(Resource):
            def post(self):
                body = request.get_json()
                item_name = body.get('item_name')
                amount = body.get('amount')
                # check if item exists on menu
                item = next((i for i in self.items if i['item'] == item_name), None)
                if item:
                    client_ip = request.remote_addr
                    if client_ip not in self.cart_items:
                        self.cart_items[client_ip] = []
                    self.cart_items[client_ip].append({'item': item, 'amount': amount})
                    return jsonify({'message': 'Item added to cart'}), 201
               
                else:
                    return jsonify({'message': 'Invalid item name'}), 400
            def get(self):
                client_ip = request.remote_addr
                if client_ip in self.cart_items:
                    return jsonify(self.cart_items[client_ip])
                else:
                    return jsonify({'message': 'No items in cart'}), 204
        api.add_resource(_Create, '/create')
        api.add_resource(_Read, '/')
        api.add_resource(_Cart, '/cart')

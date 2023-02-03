from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import time
from flask import Blueprint, request, jsonify
import json
import requests


item_api = Blueprint('item_api', __name__,
                   url_prefix='/api/item')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(item_api)

def searchItem(item):
  result_list = []
  # JSON data:
  x = {"title": "", "ingredients": "", "instructions": ""}
  
  # Request
  url = "https://recipe-by-api-ninjas.p.rapidapi.com/v1/recipe"
  querystring = {"query": item}
  headers = {
      "X-RapidAPI-Key": "cb84e1853amsh36bd127c21f5c41p12163cjsn5ce359cf2f1a",
      "X-RapidAPI-Host": "recipe-by-api-ninjas.p.rapidapi.com"
  }
  
  response = requests.request("GET", url, headers=headers, params=querystring)
  parse_req = response.json()
  for i in range(len(parse_req)):
      title = parse_req[i]["title"]
      ingredients = parse_req[i]["ingredients"]
      instructions = parse_req[i]["instructions"]
      # JSON data:
      x = {
          "title": title,
          "ingredients": ingredients,
          "instructions": instructions
      }
      with open("food.json", "a") as jsonfile:
          result_list.append(x)
          json.dump(x, jsonfile)

  return result_list



class itemAPI:
    class _Create(Resource):
        def post(self):
            body = request.get_json()
            return searchItem(body.get("item"))

    api.add_resource(_Create, '/')











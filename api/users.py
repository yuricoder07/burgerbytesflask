import json
import hashlib
from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import time
from flask import Blueprint, request, jsonify
import json
import requests

users_api = Blueprint('users_api', __name__,
                   url_prefix='/api/users')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(users_api)

#gets a number of users
def getUsers():
  # Opening JSON file
  usersList = open('users.json')
  data = json.load(usersList)
  counter = 0
  # Checks how many users are in the JSON database
  for i in data:
    counter+=1
  return(counter)



  
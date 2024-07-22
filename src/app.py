"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()

    response_body = {
        "hello": "world",
        "family": members
    }
    if len(members) == 0:
        return "No Members Found", 400
    else:
        return jsonify(response_body), 200
    
@app.route('/members/<int:id>', methods=['GET'])    
def get_family_member(id):
    get_member = jackson_family.get_member(id)
    if get_member:
        return jsonify(get_member), 200
    else:
        return "No Members Found", 400
   
    #display the individual member's information when we go to the /member/id route of the url

@app.route('/members', methods=['POST'])
def add_family_member():
    # get our values
    mem_id = request.json.get('id', jackson_family._generateId())
    mem_fname = request.json.get('first_name', None)
    mem_age = request.json.get('age', None)
    mem_lucky_numbers = request.json.get('lucky_numbers', None)

    # set object to values entered
    new_member = {
        "id": mem_id,
        "first_name": mem_fname,
        "last_name": "Jackson",
        "age": mem_age,
        "lucky_numbers": mem_lucky_numbers
        }
    
    if new_member is not None:
        # call the add.member() method on the Class object
        added_member = jackson_family.add_member(new_member)
        # return the added object
        return jsonify(added_member), 200
    else:
        return jsonify("Incorrect values in object"), 400


@app.route('/members/<int:id>', methods=['DELETE'])
def delete_family_member(id):
    # validate that we have an id
    if id:
        # what do we do if we have one?
        jackson_family.delete_member(id)
        return jsonify("Success 🥳")
    # what ELSE should we do if we don't?
    else:
        return jsonify("It didn't work...")

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

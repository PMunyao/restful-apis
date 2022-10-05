# start with a json file and dictionary that holds data objects identified using an integer id, each single id object contains 5 attributes, a, b, c, d, e wher a is name, b description, c is an enum type, d is an enum role and e miscalaneous string data. 
# write a flask restful api that gets loaded with data info and writes, deletes and update into a json file stored on github and returns the data in json format. 
# the api should be able to handle the following requests:
# GET /data/<id> - returns the data object with the given id
# POST /data - creates a new data object and returns the id of the new object
# PUT /data/<id> - updates the data object with the given id
# DELETE /data/<id> - deletes the data object with the given id
# PATCH /data/<id> - updates the data object with the given id
# GET /data - returns a list of all data objects

# create a flask app
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import json

app = Flask(__name__)
api = Api(app)
CORS(app)

data = [
    {
        "id": 1,
        "a": "Teddy",
        "b": "Bear",
        "c": "toy",
        "d": "cute",
        "e": "brown"
    },
    {
        "id": 2,
        "a": "Lion",
        "b": "King",
        "c": "animal",
        "d": "scary",
        "e": "yellow"
    },
    {
        "id": 3,
        "a": "Pig",
        "b": "Pork",
        "c": "animal",
        "d": "cute",
        "e": "pink"
    }
]

# write a flask restful api that gets loaded with data info and writes, deletes and update into a json file stored on github
class Data(Resource):
    def get(self, id):
        for d in data:
            if(d["id"] == id):
                return d, 200
        return "Data not found", 404
    
    def post(self):
        dat = {
            "id": data[-1]["id"] + 1,
            "a": request.json["a"],
            "b": request.json["b"],
            "c": request.json["c"],
            "d": request.json["d"],
            "e": request.json["e"]
        }
        data.append(dat)
        return dat, 201
    
    def put(self, id):
        for d in data:
            if(d["id"] == id):
                d["a"] = request.json["a"]
                d["b"] = request.json["b"]
                d["c"] = request.json["c"]
                d["d"] = request.json["d"]
                d["e"] = request.json["e"]
                return d, 200
        return "Data not found", 404
    
    def delete(self, id):
        for d in data:
            if(d["id"] == id):
                data.remove(d)
                return "Deleted", 200
        return "Data not found", 404
    
    def patch(self, id):
        for d in data:
            if(d["id"] == id):
                d["a"] = request.json["a"]
                d["b"] = request.json["b"]
                d["c"] = request.json["c"]
                d["d"] = request.json["d"]
                d["e"] = request.json["e"]
                return d, 200
        return "Data not found", 404

class DataList(Resource):
    def get(self):
        return data, 200

api.add_resource(Data, "/data/<int:id>")
api.add_resource(DataList, "/data")

if __name__ == "__main__":
    app.run(debug=True)

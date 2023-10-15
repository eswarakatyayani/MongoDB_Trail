from flask import Flask, Response, request, render_template, jsonify
import pymongo
import json
from bson.objectid import ObjectId

app=Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host = 'localhost',
        port = 27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.mongodb1 #connect to mongodb1
    mongo.server_info() #trigger exception if cannot connect to db
except:
    print("Error -connect to db")

@app.route('/api', methods=['POST'])
def insertdata():
  try:
    data = request.get_json()
    dbResponse = db.student.insert_one(data)
    response = Response("New Record added",status=201,mimetype='application/json')
    return response
  except Exception as ex:
    response = Response("Insert New Record Error!!",status=500,mimetype='application/json')
    return response 

@app.route('/api', methods=['GET'])
def searchall():
  try:
    documents = db.student.find()
    output = [{item: data[item] for item in data if item != '_id'} for data in documents]
    return jsonify(output)
  except Exception as ex:
    response = Response("Search Records Error!!",status=500,mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)


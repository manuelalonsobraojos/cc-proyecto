from flask import Flask
from flask import Response
from flask import jsonify, make_response
from playhouse.shortcuts import model_to_dict
from bot.model.BaseModel import db
from bot.model.Result import Result
from bot.service.ResultService import ResultService as rService
import os

db.init('dercn75nklk4a6', host='ec2-54-246-92-116.eu-west-1.compute.amazonaws.com', user='awolxnvarfbuje', password='50af008532aaf685ecf1e4bc9d397528354600f3de0a41554cf8291284b0eb93')
db.create_tables([Result])
app = Flask(__name__)


@app.route('/result')
def main():
    return 'resultados de la liga española de futbol'

@app.route('/result/get/<id>')
def getResult(id):

    result = rService.getResult(int(id))

    if(result is None):
        return jsonify(None)
    return jsonify(model_to_dict(result))

@app.route('/result/local/<local>')
def getResultBylocal(local):

    result = rService.getResultByLocal(local)

    if(result is None):
        return jsonify(None)
    return jsonify(model_to_dict(result))

@app.route('/result/visit/<visit>')
def getResultByVisit(visit):

    result = rService.getResultByVisit(visit)

    if(result is None):
        return jsonify(None)
    return jsonify(model_to_dict(result))

@app.route('/result/getall')
def getAllResult():

    result = rService.getAll()

    if(result is None):
        return jsonify(None)

    resultList= []
    for item in result:
       resultList.append(model_to_dict(item))

    return make_response(jsonify(resultList), 200)

if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

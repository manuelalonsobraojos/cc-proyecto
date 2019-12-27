from flask import Flask, Response
from flask import Response
from flask import jsonify, make_response
from playhouse.shortcuts import model_to_dict
from bot.model.BaseModel import db
from bot.model.Result import Result
from bot.service.ResultService import ResultService as rService
import os

db.init(os.environ['NAME_BD'], host=os.environ['HOST_BD'], user=os.environ['USER_BD'], password=os.environ['PASS_BD'])
db.create_tables([Result])
app = Flask(__name__)


@app.route('/result')
def main():
    return 'resultados de la liga española de futbol'

@app.route('/result/update/<id>/<rlocal>/<rvisit>', methods=['POST'])
def updateResult(id, rlocal, rvisit):

    response = rService.updateResult(id, rlocal, rvisit)

    if (response == True):
        return jsonify("true")
    else:
        return jsonify("false")

@app.route('/result/get/<id>')
def getResult(id):

    result = rService.getResult(int(id))

    if(result is None):
        return Response("404", status=404, mimetype='application/json')
    return jsonify(model_to_dict(result))

@app.route('/result/local/<local>')
def getResultBylocal(local):

    result = rService.getResultByLocal(local)

    if(result is None):
        return Response("404", status=404, mimetype='application/json')
    return jsonify(model_to_dict(result))

@app.route('/result/visit/<visit>')
def getResultByVisit(visit):

    result = rService.getResultByVisit(visit)

    if(result is None):
        return Response("404", status=404, mimetype='application/json')
        # return jsonify(None)
    return jsonify(model_to_dict(result))

@app.route('/result/delete/<id>')
def deleteResult(id):

    status = rService.deleteResult(id)
    return jsonify(status)

@app.route('/result/getall')
def getAllResult():

    result = rService.getAll()

    if(result is None):
        return Response("404", status=404, mimetype='application/json')

    resultList= []
    for item in result:
       resultList.append(model_to_dict(item))

    return make_response(jsonify(resultList), 200)

if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

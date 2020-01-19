from sanic import Sanic, response
from sanic.response import json
from playhouse.shortcuts import model_to_dict
from model.BaseModel import db
from model.Clasificacion import Clasificacion
from service.ClasificacionService import ClasificacionService as cService
import os

db.init(os.environ['NAME_BD'], host=os.environ['HOST_BD'], user=os.environ['USER_BD'], password=os.environ['PASS_BD'])
db.create_tables([Clasificacion])
app = Sanic()

@app.route("/clasificacion")
async def main(request):
    return response.json("clasificacion de la liga Española", status=200)

@app.route("/clasificacion/<pos>")
async def getClasificacionByPos(request, pos):
    clasificacion = cService.getClasificaciontByPos(int(pos))

    if(clasificacion is None):
        return response("404", status=404, mimetype='application/json')
    return response.json(model_to_dict(clasificacion), status=200)

@app.route("/clasificacion/getall")
async def getAllClasificacion(request):
    clasificacion = cService.getAll()

    if(clasificacion is None):
        return response("404", status=404, mimetype='application/json')

    clasificacionList= []
    for item in clasificacion:
       clasificacionList.append(model_to_dict(item))

    return response.json(clasificacionList, status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

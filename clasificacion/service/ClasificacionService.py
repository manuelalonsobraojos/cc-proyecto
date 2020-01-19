from model.Clasificacion import Clasificacion
import requests
from bs4 import BeautifulSoup


class ClasificacionService():

    @staticmethod
    def addClasificacion(team, points, pos):
        try:
            clasificacion = Clasificacion()
            clasificacion.setTeam(team)
            clasificacion.setPoints(points)
            clasificacion.setPos(pos)
            clasificacion.save()
            return True
        except:
            return False

    @staticmethod
    def deleteClasificacion(id):

        try:
            Clasificacion.delete_by_id(int(id))
        except:
            return False
        return True

    @staticmethod
    def getClasificaciontByPos(pos):

        try:
            clasificacion = Clasificacion.get(Clasificacion.pos == pos)
        except:
            return None
        return clasificacion

    @staticmethod
    def getAll():

        try:
            listClasificacion = []
            clasificacion = Clasificacion.select()
            for c in clasificacion:
                listClasificacion.append(c)
            result = listClasificacion
        except:
            return None
        return result

    @staticmethod
    def insertDataClasificacion():

        """Funcion que scrapea de la web la información de la clasificación de la liga española de fútbol."""

        url = "http://resultados.as.com/resultados/futbol/primera/clasificacion/"
        # Realizamos la petición a la web
        req = requests.get(url)

        # Comprobamos que la petición nos devuelve un Status Code = 200
        statusCode = req.status_code
        if statusCode == 200:

            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
            html = BeautifulSoup(req.text, "html.parser")
            # Obtenemos todos los divs donde estan las entradas
            entradas = html.find_all('span', {'class': 'nombre-equipo'})
            puntos = html.find_all('td', {'class': 'destacado'})
            v_point = []
            for i, info in enumerate(puntos):
                if i < 20:
                    v_point.insert(i, info.text)

            # Recorremos todas las entradas para extraer el título, autor y fecha
            v_team = []
            for i, entrada in enumerate(entradas):
                # Con el método "getText()" no nos devuelve el HTML
                # Sino llamamos al método "getText()" nos devuelve también el HTML
                if i < 20:
                    v_team.insert(i, entrada.text)

            for i in range(len(v_team)):
                query = Clasificacion.select().where(Clasificacion.pos == i + 1)
                if (query.exists()):
                    clasificacion = query.first()

                else:
                    clasificacion = Clasificacion()
                clasificacion.pos = i + 1
                clasificacion.team = v_team[i]
                clasificacion.points = v_point[i]
                clasificacion.save()


        else:
            print ("Status Code %d" % statusCode)

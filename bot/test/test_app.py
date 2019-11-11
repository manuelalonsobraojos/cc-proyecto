import unittest
import requests
from bot.model.BaseModel import db
from bot.model.Result import Result
from bot.service.ResultService import ResultService as rService
db.init('dercn75nklk4a6', host='ec2-54-246-92-116.eu-west-1.compute.amazonaws.com', user='awolxnvarfbuje', password='50af008532aaf685ecf1e4bc9d397528354600f3de0a41554cf8291284b0eb93')


class ResultTest(unittest.TestCase):

    def test_1(self):
        """
        Test que comprueba la búsqeuda de un reusltado por su id
        :return:
        """
        result = True

        if(rService.getResult(1) is None):
            result = False

        self.assertTrue(result)

    def test_2(self):
        """
                Test que comprueba la búqueda de un resultado por su nombre de equipo local o visitante
                :return:
                """
        result = False

        if (rService.getResultByLocal("Valencia") is not None):
            result = True
        elif (rService.getResultByVisit("Valencia") is not None):
            result = True

        self.assertTrue(result)

    def test_3(self):
        """
                Test que comprueba la búsqeuda de un resultado por su nombre de equipo visitante
                :return:
                """
        result = True

        if (rService.getResultByVisit("Granada") is None):
            result = False

        self.assertTrue(result)

    def test_4(self):
        """
        Test que comrpueba la búsqueda de todos los resultados
        :return:
        """
        result = True

        if (rService.getAll() is None):
            result = False

        self.assertTrue(result)

    def test_5(self):
        """
        Test que comrpueba la búsqueda del marcador local de un partido
        :return:
        """
        result = True

        if (rService.getResultLocal(1) is None):
            result = False

        self.assertTrue(result)

    def test_6(self):
        """
        Test que comprueba que el nombre del equipo buscado es el devuelto
        :return:
        """
        result = Result()
        name = ""
        team = "Valencia"
        if (rService.getResultByLocal("Valencia") is not None):
            result = rService.getResultByLocal("Valencia")
            name = result.getTeamLocal()
        elif (rService.getResultByVisit("Valencia") is not None):
            result = rService.getResultByVisit("Valencia")
            name = result.getTeamVisit()

        self.assertEqual(name, team)

if __name__ == '__main__':
   unittest.main()
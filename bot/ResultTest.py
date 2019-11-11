import unittest
import configparser
import os
from bot.model.BaseModel import db
from bot.service.ResultService import ResultService as rService
db.init('dercn75nklk4a6', host='ec2-54-246-92-116.eu-west-1.compute.amazonaws.com', user='awolxnvarfbuje', password='50af008532aaf685ecf1e4bc9d397528354600f3de0a41554cf8291284b0eb93')

class ResultTest(unittest.TestCase):

    def test_1(self):
        """
        Test que comprueba la búsqueda de un reusltado por su id
        :return:
        """
        result = True

        if(rService.getResult(1) is None):
            result = False

        self.assertTrue(result)

    def test_2(self):
        """
                Test que comprueba la búqueda de un resultado por su nombre de equipo local
                :return:
                """
        result = True

        if (rService.getResultByLocal("Valencia") is None):
            result = False

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

if __name__ == '__main__':
   unittest.main()
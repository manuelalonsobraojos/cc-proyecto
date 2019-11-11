import unittest
import requests
import sys
sys.path.append("../")

class ResultTest(unittest.TestCase):

    def test_1(self):
        """
        Test que comprueba la búsqueda de un reusltado por su id
        :return:
        """
        r = requests.get('http://127.0.0.1:5000/result/1')
        result = True
        if(r.json() is None):
            result = False

        self.assertTrue(result)

    def test_2(self):
        """
        Test que comprueba la búsqueda de un resultado por el nombre del equipo local
        :return:
        """
        r = requests.get('http://127.0.0.1:5000/resultlocal/Valencia')
        result = True
        if(r.json() is None):
            result = False

        self.assertTrue(result)

    def test_3(self):
        """
        Test que comprueba la búsqueda de un resultado por el nombre del equipo visitante
        :return:
        """
        r = requests.get('http://127.0.0.1:5000/resultvisit/Granada')
        result = True
        if(r.json() is None):
            result = False

        self.assertTrue(result)

    def test_4(self):
        """
        Test que comrpueba la búsqueda de todos los resultados
        :return:
        """
        r = requests.get('http://127.0.0.1:5000/resultall')
        result = True
        if (r.json() is None):
            result = False

        self.assertTrue(result)

if __name__ == '__main__':
   unittest.main()
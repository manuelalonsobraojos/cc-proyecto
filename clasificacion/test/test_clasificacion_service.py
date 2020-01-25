import unittest
from model.BaseModel import db
from model.Clasificacion import Clasificacion
from service.ClasificacionService import ClasificacionService as cService
import os
db.init(os.environ['NAME_BD'], host=os.environ['HOST_BD'], user=os.environ['USER_BD'], password=os.environ['PASS_BD'])


class ResultTest(unittest.TestCase):

    def test_check_clasificacion_by_pos(self):
        """
        Test que comprueba la búsqueda de un resultados por su id
        :return:
        """
        clasificacion = True

        if(cService.getClasificaciontByPos(1) is None):
            clasificacion = False

        self.assertTrue(clasificacion)

    def test_check_all_results(self):
        """
        Test que comprueba la búsqueda de todos los resultados
        :return:
        """
        clasificacion = True

        if (cService.getAll() is None):
            clasificacion = False

        self.assertTrue(clasificacion)


if __name__ == '__main__':
   unittest.main()

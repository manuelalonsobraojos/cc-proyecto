import unittest
from bot.model.BaseModel import db
from bot.model.Result import Result
from bot.service.ResultService import ResultService as rService
db.init(os.environ['NAME_BD'], host=os.environ['HOST_BD'], user=os.environ['USER_BD'], password=os.environ['PASS_BD'])


class ResultTest(unittest.TestCase):

    def test_check_result_by_id(self):
        """
        Test que comprueba la búsqueda de un resultados por su id
        :return:
        """
        result = True

        if(rService.getResult(1) is None):
            result = False

        self.assertTrue(result)

    def test_check_result_by_name(self):
        """
                Test que comprueba la búsqueda de un resultado por su nombre de equipo local o visitante
                :return:
                """
        result = False

        if (rService.getResultByLocal("Valencia") is not None):
            result = True
        elif (rService.getResultByVisit("Valencia") is not None):
            result = True

        self.assertTrue(result)

    def test_check_all_results(self):
        """
        Test que comprueba la búsqueda de todos los resultados
        :return:
        """
        result = True

        if (rService.getAll() is None):
            result = False

        self.assertTrue(result)

    def test_check_local_score_result(self):
        """
        Test que comprueba la búsqueda del marcador local de un partido
        :return:
        """
        result = True

        if (rService.getResultLocal(1) is None):
            result = False

        self.assertTrue(result)

    def test_name_team(self):
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

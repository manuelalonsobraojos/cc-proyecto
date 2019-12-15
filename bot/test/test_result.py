import unittest
from bot.model.BaseModel import db
from bot.model.Result import Result
db.init(os.environ['NAME_BD'], host=os.environ['HOST_BD'], user=os.environ['USER_BD'], password=os.environ['PASS_BD'])

class ResultTest(unittest.TestCase):

    def test_result_team_local(self):
        result = Result.create(teamLocal="Granada", teamVisit="Valladolid", resultLocal=1, resultVisit=1)
        self.assertEqual(result.getTeamLocal(), "Granada")

    def test_result_team_visit(self):
        result = Result.create(teamLocal="Granada", teamVisit="Valladolid", resultLocal=1, resultVisit=1)
        self.assertEqual(result.getTeamVisit(), "Valladolid")

    def test_result_local(self):
        result = Result.create(teamLocal="Granada", teamVisit="Valladolid", resultLocal=1, resultVisit=1)
        self.assertEqual(result.getResultLocal(), 1)

    def test_result_visit(self):
        result = Result.create(teamLocal="Granada", teamVisit="Valladolid", resultLocal=1, resultVisit=1)
        self.assertEqual(result.getResultVisit(), 1)

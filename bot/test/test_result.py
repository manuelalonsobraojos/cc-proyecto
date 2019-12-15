import unittest
from bot.model.BaseModel import db
from bot.model.Result import Result

class ResultTest(unittest.TestCase):

    def test_result_team_local(self):
        result = Result(teamLocal="Granada", teamVisit="Valladolid", resultLocal=1, resultVisit=1)
        self.assertEqual(result.getTeamLocal(), "Granada")

    def test_result_team_visit(self):
        result = Result(teamLocal="Granada", teamVisit="Valladolid", resultLocal=1, resultVisit=1)
        self.assertEqual(result.getTeamVisit(), "Valladolid")

    def test_result_local(self):
        result = Result(teamLocal="Granada", teamVisit="Valladolid", resultLocal=1, resultVisit=1)
        self.assertEqual(result.getResultLocal(), 1)

    def test_result_visit(self):
        result = Result(teamLocal="Granada", teamVisit="Valladolid", resultLocal=1, resultVisit=1)
        self.assertEqual(result.getResultVisit(), 1)

if __name__ == '__main__':
   unittest.main()
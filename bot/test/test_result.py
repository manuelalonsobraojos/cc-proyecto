import unittest
from bot.model.BaseModel import db
from bot.model.Result import Result
db.init('dercn75nklk4a6', host='ec2-54-246-92-116.eu-west-1.compute.amazonaws.com', user='awolxnvarfbuje', password='50af008532aaf685ecf1e4bc9d397528354600f3de0a41554cf8291284b0eb93')

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
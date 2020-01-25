import unittest
from model.BaseModel import db
from model.Clasificacion import Clasificacion

class ResultTest(unittest.TestCase):

    def test_team(self):
        clasificacion = Clasificacion(pos=1, team="Real Madrid", points=43)
        self.assertEqual(clasificacion.getTeam(), "Real Madrid")

    def test_pos(self):
        clasificacion = Clasificacion(pos=1, team="Real Madrid", points=43)
        self.assertEqual(clasificacion.getPos(), 1)

    def test_points(self):
        clasificacion = Clasificacion(pos=1, team="Real Madrid", points=43)
        self.assertEqual(clasificacion.getPoints(), 43)

if __name__ == '__main__':
   unittest.main()

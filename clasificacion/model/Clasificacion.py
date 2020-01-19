from peewee import *
from model.BaseModel import BaseModel


class Clasificacion(BaseModel):
    id = AutoField(primary_key=True)
    pos = IntegerField()
    team = CharField(max_length=50, null=False)
    points = IntegerField()

    def getId(self):
        return self.id

    def getPos(self):
        return self.pos

    def setPos(self, pos):
        self.pos = pos

    def getTeam(self):
        return self.team

    def setTeam(self, team):
        self.team = team

    def getPoints(self):
        return self.points

    def setPoints(self, points):
        self.points = points


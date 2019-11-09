from peewee import *

db = PostgresqlDatabase(None)

class Clasification(Model):
    id = AutoField(primary_key=True)
    teamLocal = CharField(max_length=50, null=False)
    teamVisit = CharField(max_length=50, null=False)
    resultLocal = IntegerField(null=True)
    resultVisit = IntegerField(null=True)
    class Meta:
        database = db
from django.db import models
from django.contrib.auth.models import User

class Scores(models.Model):
    roundnum = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(User)
    rounds_bought = models.IntegerField()
    rounds_got = models.IntegerField()
    people_paid_for = models.IntegerField()
    people_brought_coffee = models.IntegerField()
    points = models.IntegerField()

    def __unicode__(self):
        return self.buyer
    

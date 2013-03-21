from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

class Scores(models.Model):
    roundnum = models.AutoField(primary_key=True)
    buyer = models.CharField(max_length=50)
    rounds_bought = models.IntegerField()
    rounds_got = models.IntegerField()
    people_paid_for = models.IntegerField()
    people_brought_coffee = models.IntegerField()
    points = models.IntegerField()

    def __unicode__(self):
        return self.buyer
    

from django.db import models

# Create your models here.
class DataBaseHumidity(models.Model):
    data_date = models.CharField(max_length=30)
    data_value = models.IntegerField()

class DataBaseNutrients(models.Model):
    data_date = models.CharField(max_length=30)
    data_value = models.IntegerField()

class DataBaseTemperature(models.Model):
    data_date = models.CharField(max_length=30)
    data_value = models.IntegerField()

class DataBasePhosphorus(models.Model):
    data_date = models.CharField(max_length=30)
    data_value = models.IntegerField()
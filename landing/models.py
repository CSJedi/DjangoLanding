from django.db import models

class DelyveryInfo(models.Model):
    cargoName = models.CharField(max_length=200)
    shippingCost = models.FloatField()
    weight = models.FloatField()
    scope = models.FloatField()

class ProcedureInfo(models.Model):
    procedureName = models.CharField(max_length=200)
    ourContractInfo = models.CharField(max_length=200)
    yourContractInfo = models.CharField(max_length=200)

from django.db import models

class DelyveryInfo(models.Model):
    cargoName = models.CharField(max_length=200)
    shippingCost = models.FloatField()
    weight = models.FloatField()
    scope = models.FloatField()

class ProcedureInfo(models.Model):
    ProcedureName = models.CharField(max_length=200)
    OurContractInfo = models.CharField(max_length=200)
    YourContractInfo = models.CharField(max_length=200)

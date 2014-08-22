from django.db import models

class UtilityCompany(models.Model):
  name = models.CharField(max_length=200)

class LoadZone(models.Model):
  name = models.CharField(max_length=200)

class Township(models.Model):
  name = models.CharField(max_length=200)
  loadZone = models.ForeignKey(LoadZone)

class Developer(models.Model):
  name = models.CharField(max_length=200)

class LandOwner(models.Model):
  name = models.CharField(max_length=200)

class LandType(models.Model):
  name = models.CharField(max_length=200)

class Project(models.Model):
  acPower = models.IntegerField()
  angleOfRoof = models.IntegerField()
  annualPower = models.IntegerField()
  co2Offset = models.IntegerField()
  consumptionCurrent = models.IntegerField()
  consumptionGoal = models.IntegerField()
  description = models.CharField(max_length=2000)
  developer = models.ForeignKey(Developer)
  endDate = models.DateField(auto_now=False)
  greenCertificates = models.IntegerField()
  investmentCurrent = models.IntegerField()
  investmentGoal = models.IntegerField()
  landOwner = models.ForeignKey(LandOwner)
  landType = models.ForeignKey(LandType)
  location = models.CharField(max_length=200)
  milesDriven = models.IntegerField()
  moduleWatts = models.IntegerField()
  name = models.CharField(max_length=200)
  numModules = models.IntegerField()
  payback = models.CharField(max_length=200)
  powerDepreciation = models.FloatField()
  schematicUrl = models.URLField(max_length=500)
  size = models.IntegerField()
  area = models.IntegerField()
  treesSaved = models.IntegerField()
  ytm = models.CharField(max_length=200)




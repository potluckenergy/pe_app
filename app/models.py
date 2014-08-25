from django.db import models
from django.contrib.auth.models import User


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


class Settings(models.Model):
  user = models.OneToOneField(User)
  zipcode = models.CharField(max_length=200, blank=True)
  township = models.ForeignKey(Township, blank=True)



class Project(models.Model):
  initiator = models.ForeignKey(User, blank=True)
  acPower = models.IntegerField(blank=True)
  angleOfRoof = models.IntegerField(blank=True)
  annualPower = models.IntegerField(blank=True)
  co2Offset = models.IntegerField(blank=True)
  consumptionCurrent = models.IntegerField(blank=True)
  consumptionGoal = models.IntegerField(blank=True)
  description = models.CharField(max_length=2000, blank=True)
  # developer = models.ForeignKey(Developer)
  developer = models.CharField(max_length=200, blank=True)
  endDate = models.DateField(auto_now=False, blank=True)
  greenCertificates = models.IntegerField(blank=True)
  investmentCurrent = models.IntegerField(blank=True)
  investmentGoal = models.IntegerField(blank=True)
  # landOwner = models.ForeignKey(LandOwner, blank=True)
  landOwner = models.CharField(max_length=200, blank=True)
  # landType = models.ForeignKey(LandType, blank=True)
  landType = models.CharField(max_length=200, blank=True)
  location = models.CharField(max_length=200, blank=True)
  milesDriven = models.IntegerField(blank=True)
  moduleWatts = models.IntegerField(blank=True)
  name = models.CharField(max_length=200, blank=True)
  numModules = models.IntegerField(blank=True)
  payback = models.CharField(max_length=200, blank=True)
  powerDepreciation = models.FloatField(blank=True)
  schematicUrl = models.URLField(max_length=500, blank=True)
  size = models.IntegerField(blank=True)
  area = models.IntegerField(blank=True)
  treesSaved = models.IntegerField(blank=True)
  ytm = models.CharField(max_length=200, blank=True)


class Investment(models.Model):
  project = models.ForeignKey(Project)
  user = models.ForeignKey(User)
  amount = models.IntegerField()

class Consumption(models.Model):
  project = models.ForeignKey(Project)
  user = models.ForeignKey(User)
  amount = models.IntegerField()



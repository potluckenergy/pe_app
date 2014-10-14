from django.db import models
from django.contrib.auth.models import User


class UtilityCompany(models.Model):
  name = models.CharField(max_length=200)
  def __unicode__(self):
    return self.name

class LoadZone(models.Model):
  name = models.CharField(max_length=200)
  def __unicode__(self):
    return self.name

class Township(models.Model):
  name = models.CharField(max_length=200)
  loadZone = models.ForeignKey(LoadZone)
  def __unicode__(self):
    return self.name

class Developer(models.Model):
  name = models.CharField(max_length=200)
  def __unicode__(self):
    return self.name

class LandOwner(models.Model):
  name = models.CharField(max_length=200)
  def __unicode__(self):
    return self.name

class LandType(models.Model):
  name = models.CharField(max_length=200)
  def __unicode__(self):
    return self.name


class Settings(models.Model):
  user = models.OneToOneField(User)
  zipcode = models.CharField(max_length=200, blank=True)
  township = models.ForeignKey(Township, blank=True)
  def __unicode__(self):
    return self.user.email



class Project(models.Model):
  acPower = models.IntegerField(blank=True)
  angleOfRoof = models.IntegerField(blank=True)
  annualPower = models.IntegerField(blank=True)
  co2Offset = models.IntegerField(blank=True)
  consumptionCurrent = models.IntegerField(blank=True)
  consumptionGoal = models.IntegerField(blank=True)
  description = models.CharField(max_length=2000, blank=True)
  developer = models.ForeignKey(Developer, blank=True)
  endDate = models.DateField(auto_now=False, blank=True)
  greenCertificates = models.IntegerField(blank=True)
  investmentCurrent = models.IntegerField(blank=True)
  investmentGoal = models.IntegerField(blank=True)
  landOwner = models.ForeignKey(LandOwner, blank=True)
  landType = models.ForeignKey(LandType, blank=True)
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
  def __unicode__(self):
    return self.name


class Investment(models.Model):
  project = models.ForeignKey(Project)
  user = models.ForeignKey(User)
  amount = models.IntegerField()
  def __unicode__(self):
    return self.user.email

class Consumption(models.Model):
  project = models.ForeignKey(Project)
  user = models.ForeignKey(User)
  amount = models.IntegerField()
  def __unicode__(self):
    return self.user.email



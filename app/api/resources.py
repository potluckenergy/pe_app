from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields
from django.contrib.auth.models import User
from app.models import *


class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'user'
    authorization= Authorization()
    allowed_methods = ['get', 'post', 'put', 'delete']


class UtilityCompanyResource(ModelResource):
  class Meta:
    queryset = UtilityCompany.objects.all()
    resource_name = 'utilityCompany'
    authorization= Authorization()
    allowed_methods = ['get', 'post', 'put', 'delete']


class LoadZoneResource(ModelResource):
  class Meta:
    queryset = LoadZone.objects.all()
    resource_name = 'loadZone'
    authorization= Authorization()
    allowed_methods = ['get', 'post', 'put', 'delete']


class TownshipResource(ModelResource):
  class Meta:
    queryset = Township.objects.all()
    resource_name = 'township'
    authorization= Authorization()
    allowed_methods = ['get', 'post', 'put', 'delete']


class DeveloperResource(ModelResource):
  class Meta:
    queryset = Developer.objects.all()
    resource_name = 'developer'
    authorization= Authorization()
    allowed_methods = ['get', 'post', 'put', 'delete']


class LandOwnerResource(ModelResource):
  class Meta:
    queryset = LandOwner.objects.all()
    resource_name = 'landOwner'
    authorization= Authorization()
    allowed_methods = ['get', 'post', 'put', 'delete']


class LandTypeResource(ModelResource):
  class Meta:
    queryset = LandType.objects.all()
    resource_name = 'landType'
    authorization= Authorization()
    allowed_methods = ['get', 'post', 'put', 'delete']


class SettingsResource(ModelResource):
  user = fields.ForeignKey(UserResource, 'user')
  township = fields.ForeignKey(TownshipResource, 'township')
  class Meta:
    queryset = Settings.objects.all()
    resource_name = 'settings'
    authorization= Authorization()
    allowed_methods = ['get', 'post', 'put', 'delete']





class ProjectResource(ModelResource):
  class Meta:
    queryset = Project.objects.all()
    resource_name = 'project'
    authorization= Authorization()
    allowed_methods = ['get', 'post', 'put', 'delete']


class InvestmentResource(ModelResource):
  project = fields.ForeignKey(ProjectResource, 'project')
  user = fields.ForeignKey(UserResource, 'user')
  class Meta:
    queryset = Investment.objects.all()
    resource_name = 'investment'
    authorization= Authorization()
    allowed_methods = ['get', 'post', 'put', 'delete']

class ConsumptionResource(ModelResource):
  project = fields.ForeignKey(ProjectResource, 'project')
  user = fields.ForeignKey(UserResource, 'user')
  class Meta:
    queryset = Consumption.objects.all()
    resource_name = 'consumption'
    authorization= Authorization()
    allowed_methods = ['get', 'post', 'put', 'delete']













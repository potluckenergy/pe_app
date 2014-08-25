from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

from tastypie import api
from app.api.resources import *
v1_api = api.Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(UtilityCompanyResource())
v1_api.register(LoadZoneResource())
v1_api.register(TownshipResource())
v1_api.register(DeveloperResource())
v1_api.register(LandOwnerResource())
v1_api.register(LandTypeResource())
v1_api.register(SettingsResource())
v1_api.register(ProjectResource())
v1_api.register(InvestmentResource())
v1_api.register(ConsumptionResource())


urlpatterns = patterns('app.views',

    url(r'^$',          'home', name='home'),

    # backbone
    url(r'^projects',   'app', name='home'),
    url(r'^dashboard',  'app', name='home'),
    url(r'^project',    'app', name='home'),

    # auth
    url(r'^login',      'login', name='home'),
    url(r'^logout',     'logout', name='home'),

    # static
    url(r'^about',      'about', name='home'),
    url(r'^legal',      'legal', name='home'),

    # admin
    url(r'^admin/', include(admin.site.urls)),

    # api
    url(r'^api/', include(v1_api.urls)),

)

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
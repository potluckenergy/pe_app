from django.conf.urls import patterns, include, url

urlpatterns = patterns('app.views',
    url(r'^$',          'home', name='home'),
    url(r'^projects',   'home', name='home'),
    url(r'^dashboard',  'home', name='home'),
    url(r'^project',    'home', name='home'),

    # url(r'^admin/', include(admin.site.urls)),
)

"""
from django.contrib import admin
admin.autodiscover()
"""
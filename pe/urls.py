from django.conf.urls import patterns, include, url

urlpatterns = patterns('app.views',
    url(r'^$', 'home', name='home'),
    url(r'^one', 'home', name='home'),
    url(r'^two', 'home', name='home'),
    url(r'^three', 'home', name='home'),

    # url(r'^admin/', include(admin.site.urls)),
)

"""
from django.contrib import admin
admin.autodiscover()
"""
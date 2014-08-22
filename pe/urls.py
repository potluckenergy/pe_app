from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('app.views',

    url(r'^$',          'home', name='home'),

    url(r'^projects',   'app', name='home'),
    url(r'^dashboard',  'app', name='home'),
    url(r'^project',    'app', name='home'),

    url(r'^login',      'login', name='home'),
    url(r'^logout',     'logout', name='home'),

    url(r'^about',      'about', name='home'),
    url(r'^legal',      'legal', name='home'),

    url(r'^admin/', include(admin.site.urls)),

)

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
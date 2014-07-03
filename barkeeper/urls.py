from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import IndexView as index

urlpatterns = patterns(
    'barkeeper.views',

    url(r'^$', index.as_view(), name='index'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)

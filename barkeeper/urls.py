from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import IndexView, RecipesView, IngredientsView

urlpatterns = patterns(
    'barkeeper.views',

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^recipes/$', RecipesView.as_view(), name='recipes'),
    url(r'^ingredients/$', IngredientsView.as_view(), name='ingredients'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)

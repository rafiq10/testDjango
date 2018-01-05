from django.urls import path, re_path
from . import views

app_name = 'music'

urlpatterns = [
    path('',views.index, name = 'music'),
    re_path(r'^(?P<album_id>[0-9]+)/$',views.detail,name = 'details'),
    re_path(r'^(?P<album_id>[0-9]+)/favorite', views.favorite,name = 'favorite'),
]
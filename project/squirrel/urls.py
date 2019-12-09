from django.urls import path
from . import views

urlpatterns = [
        path('map/', views.map, name='map'),
        path('sightings/', views.sightings, name='sightings'),
        path('sightings/<unique_squirrel_id>/', views.update, name='update'),
        path('sightings/stats', views.stats, name='stats'),
]

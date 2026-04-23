from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single/<int:animal_id>', views.get_animal, name='single_animal'),
    path('good', views.get_animals_with_good_and_excellent_health, name='good_health_animals'),
]
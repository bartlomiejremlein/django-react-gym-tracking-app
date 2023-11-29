from django.urls import path
from gym import api

urlpatterns = [
    path("exercises/", api.exercises, name="exercises"),
    path("exercises/add/", api.add_workout, name="exercises"),
]

from django.urls import path
from gym import api

urlpatterns = [
    path("", api.test, name="test"),
]

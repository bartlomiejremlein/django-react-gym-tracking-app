from rest_framework import serializers
from gym import models


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exercise
        fields = ["id", "name"]

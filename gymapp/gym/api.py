from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from gym import serializers, models
import json


@api_view(["GET"])
def exercises(request):
    exercises = models.Exercise.objects.all()
    serializer = serializers.ExerciseSerializer(exercises, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@parser_classes([FormParser, MultiPartParser])
def add_workout(request):
    print(request.data)
    sets = json.loads(request.data["exercises"])
    workout_type = models.WorkoutType.objects.get(id=1)
    workout = models.Workout.objects.create(
        date=request.data["date"], type=workout_type
    )
    for set in sets:
        exercise = models.Exercise.objects.get(id=set["id"])
        models.Set.objects.create(
            workout=workout, exercise=exercise, reps=set["reps"], weight=set["weight"]
        )
    return Response({"request": request.data})

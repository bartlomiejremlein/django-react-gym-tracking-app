from django.db import models


# Create your models here.
class MuscleGroup(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=250, null=False)
    primary_muscle_group = models.ForeignKey(
        to=MuscleGroup, on_delete=models.CASCADE, related_name="primary"
    )
    second_muscle_group = models.ManyToManyField(
        to=MuscleGroup, related_name="secondary"
    )

    def __str__(self):
        return self.name


class WorkoutType(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Workout(models.Model):
    date = models.DateField(blank=False)
    type = models.ForeignKey(to=WorkoutType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.date} ({self.type.name})"


class Set(models.Model):
    workout = models.ForeignKey(to=Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(to=Exercise, on_delete=models.CASCADE)
    reps = models.PositiveSmallIntegerField(null=True)
    weight = models.FloatField(null=True)
    exercise_time = models.PositiveIntegerField(blank=True, null=True)
    rest_time = models.PositiveIntegerField(blank=True, null=True)
    superset = models.ForeignKey(
        to="Set", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return (
            f"{self.exercise.name} - {self.reps}x{self.weight} kg ({self.workout.date})"
        )

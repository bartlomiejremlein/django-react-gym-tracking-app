from django.contrib import admin
from gym import models


@admin.register(models.MuscleGroup)
class MuscleGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.WorkoutType)
class WorkoutTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Workout)
class WorkoutAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Set)
class SetAdmin(admin.ModelAdmin):
    pass

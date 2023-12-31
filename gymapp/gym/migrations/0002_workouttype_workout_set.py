# Generated by Django 4.2.7 on 2023-11-29 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym.workouttype')),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.PositiveSmallIntegerField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('exercise_time', models.PositiveIntegerField(null=True)),
                ('rest_time', models.PositiveIntegerField(null=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.exercise')),
                ('superset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym.set')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.workout')),
            ],
        ),
    ]

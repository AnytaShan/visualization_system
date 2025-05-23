# Generated by Django 5.2.1 on 2025-05-11 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayOfTheWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DayOfTheWeek', models.CharField(max_length=20)),
                ('EvenNotEven', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DishesName', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupsName', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'auth_groups',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentLastName', models.CharField(max_length=45)),
                ('StudentName', models.CharField(max_length=45)),
                ('GroupsID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.groups')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DayOfTheWeekId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.dayoftheweek')),
                ('DishesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.dishes')),
            ],
            options={
                'unique_together': {('DayOfTheWeekId', 'DishesId')},
            },
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectiondate', models.DateField(auto_now_add=True)),
                ('DishesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.dishes')),
                ('StudentsId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.students')),
            ],
            options={
                'unique_together': {('StudentsId', 'selectiondate')},
            },
        ),
    ]

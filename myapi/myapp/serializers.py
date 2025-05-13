from rest_framework import serializers
from .models import Groups, Dishes, DayOfTheWeek, Menu, Selection

class GroupsSerializer(serializers.ModelSerializer):
    GroupsId = serializers.IntegerField()
    GroupsName = serializers.CharField()

    class Meta:
        model = Groups
        fields = ['GroupsId', 'GroupsName']

class DishesSerializer(serializers.ModelSerializer):
    DishesId = serializers.IntegerField()
    DishesName = serializers.CharField()

    class Meta:
        model = Dishes
        fields = ['DishesId', 'DishesName']

class DayOfTheWeekSerializer(serializers.ModelSerializer):
    DayOfTheWeekId = serializers.IntegerField()
    DayOfTheWeek = serializers.CharField()
    EvenNotEven = serializers.CharField()

    class Meta:
        model = DayOfTheWeek
        fields = ['DayOfTheWeekId', 'DayOfTheWeek', 'EvenNotEven']

class MenuSerializer(serializers.ModelSerializer):
    DishesId = DishesSerializer()

    class Meta:
        model = Menu
        fields = ['DishesId']

class SelectionCountSerializer(serializers.Serializer):
    DishesId = serializers.IntegerField()
    DishesName = serializers.CharField()
    votes = serializers.IntegerField()
    
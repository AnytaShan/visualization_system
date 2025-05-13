from django.db import models

class Groups(models.Model):
    GroupsId = models.IntegerField(primary_key=True, db_column='groupsid')
    GroupsName = models.CharField(max_length=10, db_column='groupsname')

    class Meta:
        managed = False
        db_table = 'Groups'

    def __str__(self):
        return self.GroupsName

class Students(models.Model):
    StudentId = models.IntegerField(primary_key=True, db_column='studentid')
    StudentLastName = models.CharField(max_length=45, db_column='studentlastname')
    StudentName = models.CharField(max_length=45, db_column='studentname')
    GroupsID = models.IntegerField(db_column='groupsid')  # Внешний ключ как Integer

    class Meta:
        managed = False
        db_table = 'Students'

    def __str__(self):
        return f"{self.StudentLastName} {self.StudentName}"


class Dishes(models.Model):
    DishesId = models.IntegerField(primary_key=True, db_column='dishesid')
    DishesName = models.CharField(max_length=60, db_column='dishesname')

    class Meta:
        managed = False
        db_table = 'Dishes'

    def __str__(self):
        return self.DishesName


class DayOfTheWeek(models.Model):
    DayOfTheWeekId = models.IntegerField(primary_key=True, db_column='dayoftheweekid')
    DayOfTheWeek = models.CharField(max_length=20, db_column='dayoftheweek')
    EvenNotEven = models.CharField(max_length=20, db_column='evennoteven')

    class Meta:
        managed = False
        db_table = 'DayOfTheWeek'

    def __str__(self):
        return self.DayOfTheWeek


class Menu(models.Model):
    # Для составных первичных ключей в Django лучше использовать обычные поля
    id = models.AutoField(primary_key=True)  # Добавляем искусственный ключ
    DayOfTheWeekId = models.IntegerField(db_column='dayoftheweekid')
    DishesId = models.IntegerField(db_column='dishesid')

    class Meta:
        managed = False
        db_table = 'Menu'
        unique_together = ('DayOfTheWeekId', 'DishesId')


class Selection(models.Model):
    # Аналогично для составного ключа
    id = models.AutoField(primary_key=True)
    StudentsId = models.IntegerField(db_column='studentsid')
    DishesId = models.IntegerField(db_column='dishesid')
    selectiondate = models.DateField(db_column='selectiondate', auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'Selection'
        unique_together = ('StudentsId', 'selectiondate')
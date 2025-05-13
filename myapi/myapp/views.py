from django.db.models import Count
from rest_framework import generics
from .models import Groups, Menu, Selection, DayOfTheWeek
from .serializers import GroupsSerializer, MenuSerializer, SelectionCountSerializer
from datetime import date 
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response


class GroupsListView(APIView):
    def get(self, request):
        # Вариант 1: Использование connection.cursor()
        with connection.cursor() as cursor:
            cursor.execute('SELECT "groupsid", "groupsname" FROM "Groups"')
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(data)

class DailyMenuView(APIView):
    def get(self, request, day_id):
        with connection.cursor() as cursor:
            # Исправленный запрос с правильными именами столбцов
            cursor.execute("""
                SELECT m.dishesid as dish_id, d.dishesname as dish_name
                FROM "Menu" m
                JOIN "Dishes" d ON m.dishesid = d.dishesid  
                WHERE m.dayoftheweekid = %s  
            """, [day_id])
            
            columns = [col[0] for col in cursor.description]
            menu_items = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        return Response(menu_items)

class DailyVotesView(APIView):
    def get(self, request, day_id):
        selected_date = "2025-05-19"
        # selected_date = date.today().strftime('%Y-%m-%d')
        
        with connection.cursor() as cursor:
            # 1. Получаем все блюда для этого дня
            cursor.execute("""
                SELECT DISTINCT m.dishesid as dish_id, d.dishesname as dish_name
                FROM "Menu" m
                JOIN "Dishes" d ON m.dishesid = d.dishesid
                WHERE m.dayoftheweekid = %s
            """, [day_id])
            
            dishes = {row[0]: row[1] for row in cursor.fetchall()}
            
            if not dishes:  # Если нет блюд для этого дня
                return Response([])
            
            # 2. Получаем количество голосов
            query = """
                SELECT s.dishesid as dish_id, COUNT(*) as votes
                FROM "Selection" s
                WHERE s.dishesid IN %s
                AND s.selectiondate = %s
                GROUP BY s.dishesid
                ORDER BY votes DESC
            """
            cursor.execute(query, [tuple(dishes.keys()), selected_date])
            votes_data = cursor.fetchall()
        
        # 3. Формируем результат
        result = [
            {
                'DishesId': dish_id,
                'DishesName': dishes[dish_id],
                'votes': votes
            }
            for dish_id, votes in votes_data
        ]
        
        return Response(result)
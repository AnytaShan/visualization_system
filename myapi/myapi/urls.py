from django.urls import path

from myapp.views import GroupsListView, DailyMenuView, DailyVotesView

urlpatterns = [
    path('groups/', GroupsListView.as_view(), name='groups-list'),
    path('menu/<int:day_id>/', DailyMenuView.as_view(), name='daily-menu'),
    path('votes/<int:day_id>/', DailyVotesView.as_view(), name='daily-votes'),
]
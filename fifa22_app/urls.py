from django.urls import path
from .views import createeventview, createteamview, createfixtureview, userfixtureview, createquestionview

urlpatterns = [
    path('events/', createeventview.as_view(), name = 'fifa_events'),
    path('teams/', createteamview.as_view(), name = 'fifa_teams'),
    path('fixture/', createfixtureview.as_view(), name = 'fifa_fixture'),
    path('view_fixture/', userfixtureview.as_view(), name = 'fifa_user_fixture'),
    path('questions/', createquestionview.as_view(), name = 'fifa_questions'),
]

from django.urls import path
from django.contrib import admin
from .views import createteamview, createtempview#, createeventview , createfixtureview, userfixtureview, createquestionview, usereventview

urlpatterns = [
    # path('events/', createeventview.as_view(), name = 'fifa_events'),
    path('admin/', admin.site.urls),
#     path('user/viewevents/', usereventview.as_view(), name = 'fifa_events'),
    path('teams/', createteamview.as_view(), name = 'fifa_teams'),
    path('temp/', createtempview.as_view(), name = 'fifa_teams'),
#     path('fixture/', createfixtureview.as_view(), name = 'fifa_fixture'),
#     path('view_fixture/', userfixtureview.as_view(), name = 'fifa_user_fixture'),
#     path('questions/', createquestionview.as_view(), name = 'fifa_questions'),
]

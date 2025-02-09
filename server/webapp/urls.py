from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('get_user', views.get_user, name='get_user'),
    path('update_user', views.update_user, name='update_user'),
    path('get_movies', views.get_movies, name='get_movies'),
    path('all', views.all, name='all_movies'),
    path('top', views.top, name='top_movies'),
    path('calendar-events', views.get_google_calendar_events, name='calendar_events'),
    path('tasks', views.get_tasks, name='get_tasks'),
    path('tasks/create', views.create_task, name='create_task'),
    path('meetings', csrf_exempt(views.get_meetings), name='get_meetings'),
    path('meetings/create', csrf_exempt(views.create_meeting), name='create_meeting'),
    path('ai/message', views.handle_ai_message, name='ai_message'),
    path('', views.index, name='home')
]

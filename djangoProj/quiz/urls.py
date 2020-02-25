# This python file was created by me.
# This is the urls.py for the app 'quiz,' not to be confused with the urls.py in home

from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:quiz_id>/', views.detail, name = 'detail'),
    ]

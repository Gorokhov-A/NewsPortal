from django.contrib import admin
from django.urls import path
from .views import PostsList, index  # импортируем наше представление


urlpatterns = [
    # path — означает путь.
    path('index', index,),
    path('', PostsList.as_view()),
    # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
]